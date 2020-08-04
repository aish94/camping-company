from django.shortcuts import render, redirect
from blog.models import Blog, Image, Form, EventCart
from django.contrib import messages
from django.contrib.auth.models import User
from customer.models import Customer
import os
from reviews.models import BlogReview
from django.http import JsonResponse
from datetime import date, timedelta
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_blog(request):
    blogs = Blog.objects.all().order_by("-created_date")
    # try:
    #     blogs = Blog.objects.all().order_by("-created_time")
    # except Blog.DoesNotExist:
    #     blogs = None
    return render(request, "blog/all_blog.html", {"all": blogs})


def blog_detail(request, slug):
    list1 = []
    meta_des = ''
    try:
        blog = Blog.objects.get(slug=slug)
    except:
        messages.warning(request, "Blog Does not exist")
        return redirect("app:home")
    # user = User.objects.get(pk=pk)
    image_ = Image.objects.filter(blog=blog).order_by("pk")
    reviews = BlogReview.objects.filter(blog=blog)
    if reviews.count() > 0:
        page = 1
    else:
        page = 0
    try:
        review = BlogReview.objects.get(user=request.user, blog=blog)
    except:
        review = False
    for x in reviews:
        list1.append(x.rating)

    for y in image_:
        if y.content:
            for x in y.content:
                if x is not ".":
                    meta_des += x
                else:
                    meta_des += '.'
                    break
        else:
            break
    context = {
        "blog": blog,
        "image": image_,
        "reviews": reviews,
        "list1": list1,
        "page": page,
        "review": review,
        "meta_des": meta_des,
    }
    # for x in image_:
    #     print(type(x.blog_image2.url))
    return render(request, "blog/detail.html", context)


def create_blog(request):
    return render(request, "blog/create.html")


def event(request):
    return render(request, "blog/event.html")


def event_form(request):
    if request.method == "POST":
        referral = request.POST.get("referral")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        driving = request.POST.get("kyc")
        food = request.POST.get("food")
        sleep = request.POST.get("sleep")
        anything = request.POST.get("else")
        forms = Form.objects.filter(email=email)
        if forms.count() == 1:
            messages.error(request, "You already fill the form")
            return redirect("app:home")
        Form(name=name, phone=phone, referral=referral,
             email=email, driving=driving, food=food,
             sleep=sleep, anything=anything).save()
        messages.success(request, "Thanks for filling the form")
        return redirect("app:home")
    return render(request, "blog/event_form.html")


def event_pay(request):
    if request.is_ajax():
        try:
            user = User.objects.get(pk=request.user.pk)
        except:
            return JsonResponse({"signed": "false"})
        try:
            customer = Customer.objects.get(user=user)
        except:
            return JsonResponse({"customer": "false"})
        razor_id = os.environ.get("razor_id")
        amount = request.POST.get("total")
        duration = int(request.POST.get("duration"))
        check_in = request.POST.get("check_in").replace("-", "")
        check_in = datetime.datetime.strptime(check_in, "%Y%m%d").date()
        check_out = check_in + timedelta(duration)
        person_dome = request.POST.get("person_dome")
        person_roof = request.POST.get("person_roof")
        EventCart(user=user, amount=amount, email=user.email,
                  check_in=check_in,check_out=check_out,
                  person_dome=person_dome,person_roof=person_roof).save()
        name = user.username
        email = user.email
        return JsonResponse({"amount": amount, "email": email,
                             "name": name,
                             "razor_id": razor_id
                             })
    return redirect("app:home")


@login_required
def payment_failure(request):
    return render(request, "payment/failure.html")


@login_required
def payment_success(request):
    pay = EventCart.objects.filter(user=request.user).last()
    if request.is_ajax():
        txnid = request.POST.get("txnid")
        pay.txnid = txnid
        pay.save()

    return render(request, "payment/success.html", {"pay": pay})