from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tent.models import TentCheck
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from customer.models import Customer
from tent.models import TentCart
from datetime import date
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
    return render(request, "tent/tents.html")


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

        TentCart(user=user, amount=amount, email=user.email).save()
        name = user.username
        email = user.email
        return JsonResponse({"amount": amount, "email": email,
                             "name": name,
                             "razor_id": razor_id
                             })
    if price not in [99000, 110000]:
        messages.warning(request, "NO HACKY HACKY")
        return redirect("tent_check:all")
    return render(request, "tent/cart.html", {"price": price})


@login_required
def payment_failure(request):
    return render(request, "payment/failure.html")


@login_required
def payment_success(request):
    pay = TentCart.objects.filter(user=request.user).last()
    if request.is_ajax():
        txnid = request.POST.get("txnid")
        pay.txnid = txnid
        pay.save()

    return render(request, "payment/success.html", {"pay": pay})


def tent_info(request):
    return render(request,"tent/tent_info.html")