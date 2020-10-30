from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition, Book, Region
from django.contrib import messages
import datetime
from datetime import date
from app.utils import get_fields, get_val


def single_car_book(name, now, check_in, check_out):
    definition = Definition.objects.filter(car_type=name)
    for _ in definition:
        book = Book.objects.filter(definition=_, check_in_date__gte=now)
        if book.count() == 0:
            return _
        for b in book:
            if check_in < b.check_in_date and check_out < b.check_in_date or check_in > b.check_out_date \
                    and check_out > b.check_out_date:
                return _

            else:
                return {}


def multiple_car_book(name, now, check_in, check_out):
    list1 = []
    definition = Definition.objects.filter(car_type=name)
    for _ in definition:
        book = Book.objects.filter(definition=_, check_in_date__gte=now)
        if book.count() == 0:
            return _
        for b in book:
            if check_in < b.check_in_date and check_out < b.check_in_date or check_in > b.check_out_date \
                    and check_out > b.check_out_date:  # here i am checking for booked for range which is booked for,
                # meaning past dates does not matter it will always make it 1
                list1.append(1)
            else:
                list1.append(0)
        if 0 in list1:
            xenon_soft = {}
        else:
            xenon_soft = _
            break
        list1 = []
    return xenon_soft


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

    if place != "Himachal Pradesh":
        xenon_soft = multiple_car_book(name="xenon_soft", now=now, check_in=check_in, check_out=check_out)
        thar = multiple_car_book(name="thar", now=now, check_in=check_in, check_out=check_out)
        # xenon_hard = single_car_book(name="xenon_hard", now=now, check_in=check_in, check_out=check_out)
        caravan = single_car_book(name="caravan", now=now, check_in=check_in, check_out=check_out)
        xenon_soft_annex = single_car_book(name="xenon_soft_annex", now=now, check_in=check_in, check_out=check_out)
        overlanding_truck = single_car_book(name="overlanding_truck", now=now, check_in=check_in, check_out=check_out)
        force_gurkha = single_car_book(name="force_gurkha", now=now, check_in=check_in, check_out=check_out)
        data = {
            "thar": thar,
            "xenon_soft": xenon_soft,
            # "xenon_hard": xenon_hard,
            "caravan": caravan,
            "xenon_soft_annex": xenon_soft_annex,
            "overlanding_truck": overlanding_truck,
            "force_gurkha": force_gurkha,
        }
    else:
        thar = single_car_book(name="thar", now=now, check_in=check_in, check_out=check_out)
        data = {"thar": thar,
                "price": 3399}
    return render(request, "vehicle/vehicles.html", data)


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
