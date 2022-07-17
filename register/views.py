from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib import messages
from referral.models import Referral
from app.utils import *
from pay.models import Pay
import re
from django.http import JsonResponse
from register.models import Password
from datetime import date

# Create your views here.


def signup(request):
    if request.method == "POST":
        next_post = request.POST.get('next')
        if next_post == 'None':
            next_post = '/'
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_n = User.objects.filter(username=username)
        user_e = User.objects.filter(email=email)
        password1 = request.POST.get("password1")
        number = request.POST.get("phone")
        code = request.POST.get("slug")

        if len(number) > 10:
            messages.warning(request, "Phone number should be less than 10")
            return redirect("register:signin")

        if user_n.count() == 1 or user_e.count() == 1:
            messages.warning(request, "Username/email already taken or log in to complete signup")
            return redirect("register:signin")

        if code is "":

            '''If referral code is empty'''
            user = User.objects.create_user(username=username, email=email)
            Referral(user=user).save()
            user.set_password(password1)
            user.save()
            login(request, user)
            Pay(user=user, email=email, phone=number, firstname=username).save()
            Customer(user=user, phone=number, terms_condition=True).save()
            messages.success(request, "Thanks for signing up")

            message_to_company(email=email, message="someone signed up yay!! :)",
                               name=username, phone=number,
                               subject="Leads Team Rock and Roll")
            return redirect(next_post)
        try:
            ref_user = Referral.objects.get(slug=code)
        except:
            messages.warning(request, "Wrong referral code")
            return redirect("register:signin")

        '''If referral code is not empty'''
        user = User.objects.create_user(username=username, email=email)
        referral = Referral(user=user, referred_by=ref_user.user, referred=True)
        ref_user.referred_users.add(user)
        user.set_password(password1)
        user.save()
        referral.save()
        ref_user.save()
        login(request, user)
        Pay(user=user, email=email, phone=number, firstname=username).save()
        Customer(user=user, phone=number, terms_condition=True).save()
        messages.success(request, "Thanks for signing up")
        message_to_company(email=user.email, message="someone signed up yay!! :)",
                           name=username, phone=number,
                           subject="Leads Team Rock and Roll")
        message_to_customer(email)

        return redirect("app:home")

    else:
        return render(request, "register/signin.html")


def signin(request):
    next_ = request.GET.get('next')
    if request.method == "POST":
        next_post = request.POST.get('next')
        if next_post == 'None':
            next_post = '/'
        username = request.POST.get("username")
        password = request.POST.get("password")
        if re.search("@", username):
            try:
                u = User.objects.get(email=username)
                user = authenticate(username=u.username, password=password)
            except:
                messages.warning(request, "You Need to sign up first")
                return redirect("app:home")
        else:
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("app:represent")
            else:
                login(request, user)
                messages.success(request, "Logged in")
                return redirect(next_post)
        else:
            messages.warning(request, "Password/Username is wrong")
            return redirect("register:signin")
    return render(request, "register/signin.html", {"next": next_})


@login_required
def sign_out(request):
    logout(request)
    return redirect("app:home")


@login_required
def welcome(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        license_number = request.POST.get("license_number")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        city = request.POST.get("city")
        nickname = request.POST.get("nickname")
        about = request.POST.get("about")
        address = request.POST.get("address")
        user.first_name = fname
        user.last_name = lname
        user.save()
        try:
            customer = Customer.objects.get(user=user)
        except:
            messages.warning(request, "Something went wrong try again/ask the admin for help")
            return redirect("app:home")
        number = customer.phone
        Customer.objects.filter(user=user).update(city=city, address=address, nickname=nickname,
                                                  license_number=license_number, about=about)

        Pay.objects.filter(user=user).update(firstname=fname, phone=number)
        messages.success(request, "Profile fill success welcome " + str(fname))
        return redirect("customer:user_page")
    return render(request, "register/welcome.html")


def pass_reset(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({"error": "User does not exist"})
        password = Password(email=email)
        password.save()
        password_reset(name=user.first_name, email=email, subject="Password reset", link=password.reset_link)
        return JsonResponse({"success": "success"})

    slug = request.session.get("slug")

    if request.method == "POST":
        pass_resettor = Password.objects.get(slug=slug)
        user = User.objects.get(email=pass_resettor.email)
        password = request.POST.get("password1")
        user.set_password(password)
        user.save()
        pass_resettor.active = False
        pass_resettor.save()
        messages.success(request,"Password change successfully")
        return redirect("app:home")

    try:
        pass_resettor = Password.objects.get(slug=slug)
        if not pass_resettor.active and pass_resettor.used:
            del request.session["slug"]
    except:
        return render(request, "register/pass_reset.html", {"pass_resettor": {"used": False}})
    return render(request, "register/pass_reset.html", {"pass_resettor": pass_resettor})


def pass_rediretor(request,slug):
    now = date.today()
    pass_resettor = Password.objects.get(slug=slug)
    request.session["slug"] = slug
    if pass_resettor.initiate_date == now:
        pass_resettor.used = True
        pass_resettor.save()
        return redirect("register:pass_reset")
    else:
        pass_resettor.active = False
        pass_resettor.save()
    return redirect("register:pass_reset")
