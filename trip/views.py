from django.shortcuts import render, redirect
from trip.models import Trip
from tent.models import TentCheck
from vehicle.models import VehicleCheck
from equipment.models import EquipmentCheck, Inventory
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date, parse_time

# Create your views here.


def trip_create(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        check_in_date = parse_date(request.POST.get("startdate"))
        check_out_date = parse_date(request.POST.get("enddate"))
        check_in_time = parse_time(request.POST.get("starttime"))
        check_out_time = parse_time(request.POST.get("endtime"))
        duration_of_trip = request.POST.get("duration")
        amount_paid = request.POST.get("amount")
        destination = request.POST.get("destination")
        residence_address = request.POST.get("addr")
        trip_status = request.POST.get("tripstatus")
        car_type = request.POST.get("cartype")
        guest = request.POST.get("guests")

        trip = Trip(check_in_date=check_in_date, check_out_date=check_out_date,
                    check_in_time=check_in_time, check_out_time=check_out_time,
                    duration_of_trip=duration_of_trip, amount_paid=amount_paid,
                    destination=destination, residence_address=residence_address,
                    trip_status=trip_status, car_type=car_type, user=users,
                    guest=guest)
        trip.save()

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "trip/trip_create.html")


def trip_update(request, pk):
    trip = Trip.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(id=trip.user.pk)
        check_in_date = parse_date(request.POST.get("startdate"))
        check_out_date = parse_date(request.POST.get("enddate"))
        check_in_time = parse_time(request.POST.get("starttime"))
        check_out_time = parse_time(request.POST.get("endtime"))
        duration_of_trip = request.POST.get("duration")
        amount_paid = request.POST.get("amount")
        destination = request.POST.get("destination")
        residence_address = request.POST.get("addr")
        trip_status = request.POST.get("tripstatus")
        car_type = request.POST.get("cartype")
        guest = request.POST.get("guests")
        Trip.objects.filter(pk=pk).update(check_in_date=check_in_date, check_out_date=check_out_date,
                                          check_in_time=check_in_time, check_out_time=check_out_time,
                                          duration_of_trip=duration_of_trip, amount_paid=amount_paid,
                                          destination=destination, residence_address=residence_address,
                                          trip_status=trip_status, car_type=car_type, user=users,
                                          guest=guest)

        trip = Trip.objects.filter(user=users).last()
        tent = TentCheck.objects.filter(user=users).last()
        vehicle = VehicleCheck.objects.filter(user=users).last()
        equipment = EquipmentCheck.objects.filter(user=users).last()
        inventory = Inventory.objects.filter(user=users).last()
        # itinerary = Itinerary.objects.filter(user=users).last()

        if trip.trip_status == "Ended":
            trip.active = False
            tent.active = False
            vehicle.active = False
            equipment.active = False
            inventory.active = False
            # itinerary.active = False
            # itinerary.save() problem when itinerary not created
            trip.save()
            tent.save()
            vehicle.save()
            equipment.save()
            inventory.save()
        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "trip/trip_update.html", {"trip": trip})