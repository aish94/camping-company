from django.shortcuts import render, redirect
from destination.models import (Destination, Map,
                                Region, Image,
                                Amenity, Activity,
                                Detail, Circuit, Booking)
from django.http import JsonResponse
import os
import datetime
from django.contrib import messages
from datetime import date
from app.utils import invoice_message_camp

# Create your views here.


def destination(request):
    list1 = []
    maps = os.environ.get("maps")
    places = Map.objects.all().order_by("pk")
    if request.is_ajax():
        place = request.POST.get("place")
        region = Region.objects.filter(name__icontains=place)

        for x in region:
            for y in x.region.all():
                list1.append(y.pk)
        data = {"list1": list1}
        return JsonResponse(data)

    return render(request, "destination/destination.html", {"places": places, "maps": maps, "list1": list1})


def destination_detail_page(request, slug):
    # Search.objects.new_or_get(request)
    destination = Destination.objects.get(slug=slug)
    try:
        image = Image.objects.get(destination=destination)
    except:
        return render(request, "destination/detail.html", {"Data": "data available soon"})
    activity = Activity.objects.get(destination=destination)
    detail = Detail.objects.get(destination=destination)
    amenity = Amenity.objects.get(destination=destination)
    place = destination.place
    place = 'kdestinationk' + place
    place = place.replace(" ", "-")
    context = {
               "image": image,
               "destination": destination,
               "amenity": amenity,
               "activity": activity,
               "detail": detail,
               "place": place
               }

    if request.is_ajax():
        if request.user.is_authenticated:
            days = int(request.POST.get("number"))
            caravan = int(request.POST.get("Caravan")) * days
            ground = int(request.POST.get("Ground")) * days
            rooftop = int(request.POST.get("Rooftop")) * days
            dates = datetime.datetime.strptime(request.POST.get("date"), "%Y-%m-%d").date()
            amount = caravan + ground + rooftop
            igst = amount*.18
            convenient = amount*.024
            amount += igst + convenient
            Booking(destination=detail, user=request.user,
                    caravan=caravan, ground=ground, rooftop=rooftop,
                    days=days, date=dates, amount=amount, igst=igst,
                    convenient=convenient).save()
            return JsonResponse({"amount": amount, "email": request.user.email,
                                 "name": request.user.first_name,
                                 "razor_id": os.environ.get("razor_id")
                                 })
        else:
            return redirect("register:signup")

    return render(request, "destination/detail.html", context)


def circuits(request):
    return render(request, "destination/circuits.html")


def circuit(request, slug):
    cir = Circuit.objects.get(slug=slug)
    return render(request, "destination/circuit.html", {"cir": cir})


def success(request):
    now = date.today().strftime("%Y-%m-%d")
    try:
        book = Booking.objects.filter(user=request.user).last()
    except:
        messages.warning(request, "Book a campsite first")
        return redirect("app:home")
    if request.is_ajax():
        txnid = request.POST.get("txnid")
        book.txnid = txnid
        book.save()
        duration = book.days
        caravan = book.caravan
        ground = book.ground
        rooftop = book.rooftop
        txnid = book.txnid
        total = book.amount
        count = book.pk
        email = book.user.email
        name = book.user.first_name
        igst = book.igst
        convenient = book.convenient
        invoice_message_camp(email,  os.environ.get("email"),
                             txnid=txnid, now=now, name=name, convenient=convenient, total=total, duration=duration,
                             count=count, igst=igst, caravan=caravan, ground=ground, rooftop=rooftop)

    return render(request, "destination/success.html", {"book": book})