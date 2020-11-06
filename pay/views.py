import math
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pay.models import Pay
from customer.models import Customer
from vehicle.models import Book, Definition
from datetime import date, timedelta
import datetime
import os
from app.utils import invoice_message

# Create your views here.


@login_required
def payment_success(request):
    now = date.today().strftime("%Y-%m-%d")
    try:
        pay = Pay.objects.get(user=request.user)
    except:
        messages.warning(request, "Book a car first")
        return redirect("app:home")
    if request.is_ajax():
        duration = int(request.POST.get("duration"))
        check_in = request.POST.get("check_in").replace("-", "")
        check_in = datetime.datetime.strptime(check_in, "%Y%m%d").date()
        check_out = check_in + timedelta(duration)
        car_id = request.POST.get("car_id")
        definition = Definition.objects.get(pk=car_id)
        txnid = request.POST.get("txnid")
        pay.txnid = txnid
        pay.save()
        Book(user=request.user,
             definition=definition,
             check_out_date=check_out,
             check_in_date=check_in,
             duration=duration, txnid=txnid).save()

        book = Book.objects.get(user=request.user, txnid=txnid)
        car = pay.car_price
        duration = book.duration
        txnid = pay.txnid
        name = pay.firstname
        person = pay.person_price
        campkit = pay.campkit
        gas = pay.gas_stove
        torch = pay.torch
        table = pay.table
        igst = pay.igst
        convenient = pay.convenient
        chair = pay.chair
        total = pay.amount
        count = book.pk
        coupon = pay.coupon
        shillong = pay.shillong_transfer
        airport = pay.airport_transfer

        invoice_message(pay.email, os.environ.get("email"),
                        car=car, duration=duration, txnid=txnid,
                        now=now, name=name, person=person, campkit=campkit,
                        gas=gas, torch=torch, table=table,
                        igst=igst, convenient=convenient, chair=chair,total=total,
                        count=count, coupon=coupon, shillong=shillong, airport=airport)

    return render(request, "payment/success.html", {"pay": pay})


@login_required
def payment_failure(request):
    return render(request, "payment/failure.html")


@login_required
def cart(request):
    user = User.objects.get(pk=request.user.pk)
    try:
        customer = Customer.objects.get(user=user)
    except:
        messages.warning(request, "Complete Sign up")
        return redirect("register:welcome")
    razor_id = os.environ.get("razor_id")
    if not request.is_ajax():
        try:
            price = int(request.POST.get("price"))
        except:
            return redirect("app:home")
    if request.is_ajax():
        amount = math.ceil(float(request.POST.get("total")))
        car_price = request.POST.get("car_price")
        person_price = math.ceil(float(request.POST.get("person_price")))
        campkit = math.ceil(float(request.POST.get("campkit")))
        gas_stove = math.ceil(float(request.POST.get("gas_stove")))
        torch = math.ceil(float(request.POST.get("torch")))
        chair = math.ceil(float(request.POST.get("chair")))
        table = math.ceil(float(request.POST.get("table")))
        igst = float(request.POST.get("igst"))
        convenient = float(request.POST.get("convenient"))
        coupon = float(request.POST.get("coupon"))
        shillong_transfer = float(request.POST.get("shillong"))
        airport_transfer = float(request.POST.get("airport"))

        Pay.objects.filter(user=user).update(amount=amount, car_price=car_price,
                                             person_price=person_price, campkit=campkit,
                                             gas_stove=gas_stove, torch=torch, chair=chair, table=table,
                                             igst=igst, convenient=convenient, coupon=coupon,
                                             shillong_transfer=shillong_transfer, airport_transfer=airport_transfer)
        payment = Pay.objects.get(user=user)
        name = payment.firstname
        email = payment.email
        return JsonResponse({"amount": amount, "email": email,
                             "name": name,
                             "razor_id": razor_id
                             })
    return render(request, "payment/cart.html", {"price": price})
