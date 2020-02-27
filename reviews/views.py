from django.shortcuts import render, redirect
from reviews.models import DestinationReview, BlogReview
from destination.models import Destination
from blog.models import Blog
from django.http import JsonResponse
from datetime import date, timedelta
import datetime
from django.contrib import messages

# Create your views here.


def destination_add_review(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            des = Destination.objects.get(slug=request.POST.get("slug"))
            rating = request.POST.get("star")
            comment = request.POST.get("comment")
            DestinationReview(user=request.user, destination=des, comment=comment, rating=rating, rated=True).save()
            return JsonResponse({"saved": "success"})
        else:
            return JsonResponse({"not saved": "failure"})
    messages.warning(request, "Oh no You are lost mate!!!")
    return redirect("app:home")


def blog_add_review(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            blog = Blog.objects.get(slug=request.POST.get("slug"))
            rating = request.POST.get("star")
            comment = request.POST.get("comment")
            BlogReview(user=request.user, blog=blog, comment=comment, rating=rating, rated=True).save()
            return JsonResponse({"saved": "success"})
        else:
            return JsonResponse({"not saved": "failure"})
    messages.warning(request, "Oh no You are lost mate!!!")
    return redirect("app:home")