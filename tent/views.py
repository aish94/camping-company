from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tent.models import TentCheck
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from customer.models import Customer
from tent.models import TentCart, Tent, TentImage
from datetime import date
from app.utils import invoice_message_tent
import os
import math


# Create your views here.


def tent_create_check(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")

        tent = TentCheck(rod=rod, mattress=mattress, zip=zip,
                         rain_cover=rain_cover, ladder=ladder, straps=straps,
                         user=users)
        tent.save()
        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "tent/tent_create_check.html")


def tent_update_check(request, pk):
    tent = TentCheck.objects.get(pk=pk)
    if request.method == "POST":
        users = User.objects.get(pk=tent.user.pk)
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")

        TentCheck.objects.filter(pk=pk).update(rod=rod, mattress=mattress, zip=zip,
                                               rain_cover=rain_cover, ladder=ladder, straps=straps,
                                               user=users)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "tent/tent_update_check.html", {"tent": tent})


def tents(request):
    tents = Tent.objects.all().order_by("-pk")
    return render(request, "tent/tents.html", {'tents': tents})


@login_required
def cart(request, slug):
    user = User.objects.get(pk=request.user.pk)
    tent = Tent.objects.get(slug=slug)
    try:
        customer = Customer.objects.get(user=user)
    except:
        messages.warning(request, "Complete Sign up")
        return redirect("register:welcome")
    razor_id = os.environ.get("razor_id")
    if request.is_ajax():
        amount = math.ceil(float(request.POST.get("total")))
        igst = math.ceil(float(request.POST.get("igst")))
        coupon = math.ceil(float(request.POST.get("coupon")))
        convenient = math.ceil(float(request.POST.get("convenient")))
        ladder = math.ceil(float(request.POST.get("convenient")))
        shipping = math.ceil(float(request.POST.get("shipping")))
        tent = math.ceil(float(request.POST.get("tent")))

        TentCart(user=user, amount=amount, email=user.email,
                 ladder=ladder, shipping=shipping,
                 coupon=coupon, convenient=convenient, igst=igst,
                 tent=tent).save()
        name = user.username
        email = user.email
        return JsonResponse({"amount": amount, "email": email,
                             "name": name,
                             "razor_id": razor_id
                             })
    return render(request, "tent/cart.html", {"tent": tent})


@login_required
def payment_failure(request):
    return render(request, "payment/failure.html")


@login_required
def payment_success(request):
    now = date.today().strftime("%Y-%m-%d")
    pay = TentCart.objects.filter(user=request.user).last()
    if request.is_ajax():
        txnid = request.POST.get("txnid")
        pay.txnid = txnid
        pay.save()

        igst = pay.igst
        coupon = pay.coupon
        convenient = pay.convenient
        ladder = pay.ladder
        shipping = pay.shipping

        count = pay.pk
        amount = pay.amount
        tent = pay.tent
        invoice_message_tent(pay.email, os.environ.get("email"),tent=tent,
                             txnid=txnid, now=now, name=pay.user.username,
                             igst=igst, convenient=convenient, total=amount,
                             count=count, coupon=coupon,
                             ladder=ladder, shipping=shipping)

    return render(request, "payment/success.html", {"pay": pay})


def tent_info(request, slug):
    tent = Tent.objects.get(slug=slug)
    tent_images = TentImage.objects.filter(tent=tent)
    return render(request,"tent/tent_info.html", {'tent': tent, 'tent_images': tent_images})