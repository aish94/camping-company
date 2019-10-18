from django.shortcuts import render, redirect
from genie.models import VehiclePhoto, Cleanliness, PhotoId
from vehicle.models import Book
from customer.models import Customer
from django.contrib import messages
from datetime import date

# Create your views here.


def index(request):
    now = date.today()
    book = Book.objects.filter(check_in_date__gte=now)
    return render(request, "genie/index.html", {"book": book})


def create(request, pk):
    book = Book.objects.get(pk=pk)
    vehicle = VehiclePhoto.objects.filter(book=book)
    if vehicle.count() >= 1:
        messages.warning(request, "Already uploaded updation will come soon")
        return redirect("genie:index")

    if request.method == 'POST':
        # Car images

        front = request.FILES['front']
        back = request.FILES['back']
        side1 = request.FILES['side1']
        side2 = request.FILES['side2']

        # Cleanliness
        inside_tent = request.FILES['inside_tent']
        inside_car = request.FILES['inside_car']
        outside_car = request.FILES['outside_car']

        # id
        id1 = request.FILES['inside_tent']
        id2 = request.FILES['inside_car']
        id3 = request.FILES['outside_car']
        id4 = request.FILES['outside_car']
        id5 = request.FILES['outside_car']

        VehiclePhoto(book=book, front=front, back=back, side1=side1, side2=side2).save()
        Cleanliness(book=book, inside_tent=inside_tent, inside_car=inside_car, outside_car=outside_car).save()
        PhotoId(book=book, id1=id1, id2=id2, id3=id3, id4=id4, id5=id5).save()
        messages.success(request, "Saved image success")
        return redirect("genie:index")

    return render(request, "genie/create.html")


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
