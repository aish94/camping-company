from django.shortcuts import render, redirect
from blog.models import Blog, Image, Form
from django.contrib import messages
from reviews.models import BlogReview

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