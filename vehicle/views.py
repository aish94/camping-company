from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition, Book, Region
from django.contrib import messages
import datetime
from datetime import date
from app.utils import get_fields, get_val


def car_book(now, check_in, check_out):
    car_ids = []
    definition = Definition.objects.all()
    for _ in definition:
        t = 0
        if not _.available:
            continue
        book = Book.objects.filter(definition=_, check_in_date__gte=now).order_by("year")
        if book.count() == 0:
            car_ids.append(_.pk)
            continue
        for b in book:
            if check_out < b.check_in_date or check_in > b.check_out_date:
                t += 1
        if t == book.count():
            car_ids.append(_.pk)
    return car_ids


def vehicles(request):
    now = date.today()
    place = request.GET.get("place")
    try:
        d0 = request.GET.get("tripDay").replace("-", "")
    except:
        return redirect("app:home")
    duration = int(request.GET.get("Duration"))
    if duration <= 0:
        messages.warning(request, "Woops!! days should be greater than 0")
        return redirect("app:home")
    check_in = datetime.datetime.strptime(d0, "%Y%m%d").date()
    check_out = check_in + datetime.timedelta(duration)

    if check_in < now:
        messages.warning(request, "cant book the car for past date")
        return redirect("app:home")

    car_ids = car_book(now, check_in, check_out)
    cars = Definition.objects.filter(pk__in=car_ids)
    return render(request, "vehicle/vehicles.html", {"cars": cars})


def vehicle_info(request):
    return render(request, "vehicle/vehicle_info.html")


def vehicle(request):
    cars = Definition.objects.all()
    region = Region.objects.all()
    if request.method == "POST":
        r = request.POST.get("region")
        try:
            region = Region.objects.get(name=r)
            cars = region.cars.all()
            region = Region.objects.all()
        except:
            messages.warning(request, "Invalid region/region does not exist")
            return redirect("vehicle:vehicle")
        return render(request, "vehicle/vehicle.html", {"cars": cars, "region": region})
    return render(request, "vehicle/vehicle.html", {"cars": cars, "region": region})


def vehicle_create_check(request, pk):
    users = User.objects.get(id=pk)
    input_data = get_fields(VehicleCheck())
    input_data_list = input_data[2:len(input_data)-1]
    if request.method == "POST":
        data = get_val(request=request, body=input_data_list)
        VehicleCheck(user=users, **data).save()
        return redirect("app:show_status", pk=users.pk)
    else:
        return render(request, "vehicle/vehicle_create_check.html")


def vehicle_update_check(request, pk):
    v = VehicleCheck.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(pk=v.user.pk)
        input_data = get_fields(VehicleCheck())
        input_data_list = input_data[2:len(input_data) - 1]
        data = get_val(request=request, body=input_data_list)
        VehicleCheck.objects.filter(pk=pk).update(user=users, **data)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "vehicle/vehicle_update_check.html", {"vehicle": v})
