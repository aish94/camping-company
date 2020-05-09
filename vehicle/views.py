from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition, Book
from django.contrib import messages
import datetime
from datetime import date


# Create your views here.

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
    duration = request.GET.get("Duration")
    check_in = datetime.datetime.strptime(d0, "%Y%m%d").date()
    check_out = check_in + datetime.timedelta(int(duration))

    if check_in < now:
        messages.warning(request, "cant book the car for past date")
        return redirect("app:home")

    if place != "Himachal Pradesh":
        xenon_soft = multiple_car_book(name="xenon_soft", now=now, check_in=check_in, check_out=check_out)
        thar = multiple_car_book(name="thar", now=now, check_in=check_in, check_out=check_out)
        xenon_hard = single_car_book(name="xenon_hard", now=now, check_in=check_in, check_out=check_out)
        caravan = single_car_book(name="caravan", now=now, check_in=check_in, check_out=check_out)
        xenon_soft_annex = single_car_book(name="xenon_soft_annex", now=now, check_in=check_in, check_out=check_out)
        overlanding_truck = single_car_book(name="overlanding_truck", now=now, check_in=check_in, check_out=check_out)
        data = {
            "thar": thar,
            "xenon_soft": xenon_soft,
            "xenon_hard": xenon_hard,
            "caravan": caravan,
            "xenon_soft_annex": xenon_soft_annex,
            "overlanding_truck": overlanding_truck
        }
    else:
        thar = single_car_book(name="thar", now=now, check_in=check_in, check_out=check_out)
        data = {"thar": thar,
                "price": 3399}
    return render(request, "vehicle/vehicles.html", data)


def vehicle_info(request):
    return render(request, "vehicle/vehicle_info.html")


def vehicle(request):
    return render(request, "vehicle/vehicle.html")


def vehicle_create_check(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        engine_oil_level = request.POST.get("engine_oil")
        brake_fluid_level = request.POST.get("brake_fluid")
        water_level = request.POST.get("water_level")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        vehicle = VehicleCheck(user=users, engine_oil_level=engine_oil_level,
                               brake_fluid_level=brake_fluid_level, water_level=water_level,
                               windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                               parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                               burning_smell=burning_smell, steering_alignment=steering_alignment,
                               dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                               leakage=leakage)
        vehicle.save()
        return redirect("app:show_status", pk=users.pk)
    else:
        return render(request, "vehicle/vehicle_create_check.html")


def vehicle_update_check(request, pk):
    vehicle = VehicleCheck.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(pk=vehicle.user.pk)
        engine_oil_level = request.POST.get("engine_oil")
        brake_fluid_level = request.POST.get("water_level")
        water_level = request.POST.get("brake_fluid")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        VehicleCheck.objects.filter(pk=pk).update(user=users, engine_oil_level=engine_oil_level,
                                                  brake_fluid_level=brake_fluid_level, water_level=water_level,
                                                  windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                                                  parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                                                  burning_smell=burning_smell, steering_alignment=steering_alignment,
                                                  dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                                                  leakage=leakage)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "vehicle/vehicle_update_check.html", {"vehicle": vehicle})
