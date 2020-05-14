from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from equipment.models import Inventory
from customer.models import Customer
from trip.models import Trip
from django.contrib import messages
from django.http import JsonResponse
from vehicle.models import Book
import os
from django.utils import timezone

from app.utils import *

# Create your views here.


def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def all_user(request):
    users = User.objects.all()
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email)
        return render(request, "app/all_user.html", {"users": user})
    return render(request, "app/all_user.html", {"users": users})


def detail_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        customer = Customer.objects.get(user=user)
    except:
        messages.warning("This user is before initial signup/because of new signup not available")
        return redirect("app:all_user")
    if request.is_ajax():
        lead_status = request.POST.get("lead_status")
        Customer.objects.filter(user=user).update(
            lead_status=lead_status)
        return JsonResponse({"data": lead_status})
    return render(request, "app/user_detail.html", {"customer": customer})


def terms_condition(request):
    return render(request, "app/terms_condition.html")


def calender(request):
    if request.user.is_superuser:
        x = Trip.objects.filter(trip_status="ongoing")
        y = Trip.objects.filter(trip_status="ongoing")

        for thar in x:
            thar = thar

        for xenon in y:
            xenon = xenon

        if x.count() == 1 and y.count() == 1:
            context = {
                "thar": thar,
                "Xenon": xenon
            }
        else:
            raise Http404("You Did not have save previous trips as ended please fix and try again")

        return render(request, "app/calender.html", context)

    else:
        return redirect("customer:user_page")


def findus(request):
    if request.method == "POST":
        x = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={"secret": os.environ.get("GOOGLE_SERVER_CAPTCHA"),
                  "response": request.POST.get('g-recaptcha-response'),
                  })
        if x.status_code == 200:
            x = x.json()
            if x["success"]:
                email = str(request.POST.get("email"))
                name = str(request.POST.get("name"))
                phone = str(request.POST.get("phone"))
                subject = "Query"
                message = str(request.POST.get("message"))
                message_to_company(name, email, subject, message, phone)
                message_to_customer(email)
                messages.success(request, "Your message sent")
                return redirect("app:findus")
            else:
                messages.warning(request, "Captcha incorrect try agian")
                return redirect("app:findus")

    else:
        return render(request, "app/findus.html", {"g": os.environ.get("GOOGLE_CLIENT_CAPTCHA")})


@login_required
def show_status(request, pk):
    # put active everywhere not only in trip status because if not trip can be
    if request.user.is_superuser:
        users = User.objects.get(pk=pk)
        trcount = users.trip_check.filter(user=users, active=True).count()
        ecount = users.equipment_check.filter(user=users, active=True).count()
        vcount = users.vehicle_check.filter(user=users, active=True).count()
        tcount = users.tent_check.filter(user=users, active=True).count()
        icount = users.inventory.filter(user=users, active=True).count()
        return render(request, "app/show.html", {"users": users, "ecount": ecount,
                                                 "tcount": tcount, "vcount": vcount,
                                                 "trcount": trcount, "icount": icount})
    else:
        return redirect("customer:user_page")


@login_required
def represent(request):
    if request.user.is_superuser:
        if request.is_ajax():
            email = request.POST.get("email")
            try:
                user = User.objects.get(email=email)
                pk = user.pk
                data = {
                    "id": pk
                }
                return JsonResponse(data)
            except:
                data = {
                    "id": 0
                }
                return JsonResponse(data)
        super_user = request.user
        trips = Trip.objects.filter(active=True)
        inventory = Inventory.objects.filter(active=True)
        users = User.objects.all()
        context = {
            "trips": trips,
            "users": users,
            "inventorys": inventory,
            "super_user": super_user
        }
        return render(request, "app/represent.html", context)
    else:
        return redirect("customer:user_page")


def faq(request):
    return render(request, "app/faq.html")


def damage_charges(request):
    return render(request, "app/damage_charges.html")


def sitemap(request):
    return render(request, "app/sitemap.xml")
