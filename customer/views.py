from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from destination.models import Destination
from .models import Customer, Form
from itinerary.models import Itinerary
from referral.models import Referral
from django.contrib.auth.models import User
import requests
from django.contrib import messages
import os
# Create your views here.


# def destination(request):
#     return render(request, "customer/create_itinerary.html")

def simple_message(name, email, subject, message):
    return requests.post(
        os.environ.get("MAILGUN_URL"),
        auth=("api", os.environ.get("MAILGUN_API_KEY")),
        data={"from": os.environ.get("MAILGUN_FROM"),
              "to": os.environ.get("email"),
              "subject": subject,
              "text": "Name of the person queried : {} \nEmail of the person queried : "
                      "{} \nQuery : {}".format(name, email, message)
              })


@login_required
def user_page(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except:
        messages.warning(request, "Please log in first")
        return redirect("app:home")
    if customer.license_number is None:
        messages.warning(request, "Please complete sign up")
        return redirect("register:welcome")
    user = User.objects.get(username=customer.user.username)
    referral = Referral.objects.get(user=user)
    # print(referral.referral_link)
    return render(request, "customer/user_page.html", {"customer": customer, "referral": referral})


@login_required
def create_itinerary(request):
    # Search.objects.new_or_get(request)
    items = Destination.objects.all()
    itinerary = Itinerary.objects.filter(user=request.user, active=True).count()
    if itinerary == 0:
        context = {"items": items, "itinerary": itinerary}
        return render(request, "customer/create_itinerary.html", context)
    else:
        return render(request, "customer/create_itinerary.html", {"items": items, "itinerary": itinerary})


@login_required
def delete_itinerary(request):
    itinerary = Itinerary.objects.filter(user=request.user, active=True)
    if itinerary.count() == 0:
        messages.warning(request, "No itinerary found create one")
        return redirect("customer:user_page")
    elif itinerary.count() == 1:
        itinerary.delete()
        messages.success(request, "successfully deleted")
    return redirect("customer:user_page")


@login_required
def trip_detail(request):
    users = User.objects.get(pk=request.user.pk)
    return render(request, "customer/trip_status.html", {"users": users})


@login_required
def custom_itinerary(request):
    data = Itinerary.objects.filter(user=request.user, active=True)
    list1 = []
    list2 = []
    hour = 12
    for x in data:
        for y in x.destination.all():
            if hour-y.hours >= 0:
                list2.append(y.pk)
                hour = hour - y.hours
            else:
                list1.append(list2)
                list2 = []
                list2.append(y.pk)
                hour = 12
        list1.append(list2)

    if request.is_ajax():
        message = request.POST.get("places")
        list1 = [int(s) for s in message.split(',')]
        itinerary = Itinerary(user=request.user)
        itinerary.save()
        for x in list1:
            destination = Destination.objects.get(pk=x)
            itinerary.destination.add(destination)
    return render(request, "customer/custom.html", {"data": data, "list": list1})


@login_required
def book(request, pk):
    user = User.objects.get(pk=pk)
    email = str(user.email)
    name = str(user.first_name)
    subject = str("Booking")
    message = str("{} just Booked a car :D name {} phone {}".format(name, user.first_name, user.customer_check.phone))
    simple_message(name, email, subject, message)
    return render(request, "customer/success.html")


@login_required
def form(request):
    user = User.objects.get(pk=request.user.pk)
    forms = Form.objects.filter(user=user)
    if forms.count() == 1:
        messages.warning(request, "You already fill the form Thanks")
        return redirect("app:home")

    if request.method == "POST":
        companion = request.POST.get("partner")
        people = request.POST.get("people")
        expectations = request.POST.get("experience")
        overlanding = request.POST.get("overlanding")
        itinerary = request.POST.get("itinerary")
        Form.objects.get_or_create(user=user, people=people, companion=companion,
                                   expectations=expectations, overlanding=overlanding,
                                   itinerary=itinerary)
        messages.success(request, "Thanks for filling the form")
        return redirect("customer:user_page")
    return render(request, "customer/user_form.html")