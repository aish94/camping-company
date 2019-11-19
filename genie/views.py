from django.shortcuts import render, redirect
from genie.models import VehiclePhoto, Cleanliness, PhotoId
from vehicle.models import Book
from django.contrib.auth.models import User
from vehicle.models import Definition
from django.contrib import messages
from datetime import date
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from app.utils import compress

# Create your views here.


@login_required
def index(request):
    now = date.today() - timedelta(days=14) # suppose date is 15 subtract 14 and display all books greator than =1
    book = Book.objects.filter(check_in_date__gte=now)
    return render(request, "genie/index.html", {"book": book})


@login_required
def create(request, pk):
    book = Book.objects.get(pk=pk)
    vehicle = VehiclePhoto.objects.filter(book=book)
    if vehicle.count() >= 1:
        messages.warning(request, "Already uploaded updation will come soon")
        return redirect("genie:index")

    if request.method == 'POST':
        # Car images

        front = compress(request.FILES['front'])
        back = compress(request.FILES['back'])
        side1 = compress(request.FILES['side1'])
        side2 = compress(request.FILES['side2'])

        # Cleanliness
        inside_tent = request.FILES['inside_tent']
        inside_car = request.FILES['inside_car']
        outside_car = request.FILES['outside_car']

        # id
        id1 = request.FILES['id1']
        id2 = request.FILES['id2']
        id3 = request.FILES['id3']
        id4 = request.FILES['id4']
        id5 = request.FILES['id5']

        VehiclePhoto(book=book, front=front, back=back, side1=side1, side2=side2).save()
        Cleanliness(book=book, inside_tent=inside_tent, inside_car=inside_car, outside_car=outside_car).save()
        PhotoId(book=book, id1=id1, id2=id2, id3=id3, id4=id4, id5=id5).save()
        messages.success(request, "Saved image success")
        return redirect("genie:index")

    return render(request, "genie/create.html")


@login_required
def show(request, pk):
    book = Book.objects.get(pk=pk)
    try:
        vehicle = VehiclePhoto.objects.get(book=book)
        clean = Cleanliness.objects.get(book=book)
        ids = PhotoId.objects.get(book=book)
    except:
        messages.warning(request, "there is no image")
        return redirect("genie:index")
    return render(request, "genie/show.html", {"vehicle": vehicle,
                                               "book": book, "clean": clean,
                                               "ids": ids})


@login_required
def offline(request):
    if request.method == "POST":
        check_in = datetime.datetime.strptime(request.POST.get("check_in"), "%Y-%m-%d").date()
        check_out = datetime.datetime.strptime(request.POST.get("check_out"), "%Y-%m-%d").date()
        duration = int(request.POST.get("duration"))
        txnid = request.POST.get("txnid")
        username = request.POST.get("username")
        defi = request.POST.get("definition")
        definition = Definition.objects.get(car_name=defi)
        user = User.objects.get(username=username)
        Book(user=user, definition=definition, car_name=definition.car_name,
             check_in_date=check_in, check_out_date=check_out, duration=duration, txnid=txnid).save()
        messages.success(request, "Book saved success")
        return redirect("genie:index")
    return render(request, "genie/offline.html")
