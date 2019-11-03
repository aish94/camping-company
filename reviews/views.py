
from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import reviews
from .forms import ReviewForm
from destination.models import Destination
import datetime

def review(request):
    latest_review_list = reviews.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}

    return render(request, 'reviews/reviews.html', context)

def add_review(request):
    destination = Destination.objects.get(pk=1)
    if (request.method=='POST'):
        user_name=request.POST.get("name")
        email=request.POST.get("email")
        comment=request.POST.get("comment")
        rating=int(request.POST.get("rating"))
        reviews(destination=destination, user_name=user_name, email=email, comment=comment, rating=rating).save()


    #if form.is_valid():
        #rating = form.cleaned_data['rating']
        #comment = form.cleaned_data['comment']
        #user_name = form.cleaned_data['user_name']
        #review = reviews()
        #review.destination = destination
        #review.user_name = user_name
        #review.rating = rating
        #review.comment = comment
        #review.pub_date = datetime.datetime.now()
        #review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('reviews:reviews', args=(destinat)))

    return render(request, 'reviews/add_review.html')

def Show(request):
    all_review_list = reviews.objects.order_by('-pub_date')
    context = {'all_review_list':all_review_list}
    return render(request, 'reviews/show.html', context)


def review_list(request):
    latest_review_list = reviews.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(reviews, pk=review_id)
    return render(request, 'reviews/review_list.html', {'review': review})


def destination_list(request):
    destination_list = Destination.objects.order_by('-name')
    context = {'destination_list':destination_list}
    return render(request, 'reviews/circuits.html', context)


def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'reviews/detail.html', {'campsite': campsite})
