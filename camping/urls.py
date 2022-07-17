"""camping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls", namespace="app")),
    path('equipment/', include("equipment.urls", namespace="equipment")),
    path('tent/', include("tent.urls", namespace="tent")),
    path('trip/', include("trip.urls", namespace="trip")),
    path('vehicles/', include("vehicle.urls", namespace="vehicle")),
    path('accounts/', include("register.urls", namespace="register")),
    path('user/', include("customer.urls", namespace="customer")),
    path('blog/', include("blog.urls", namespace="blog")),
    path('referral/', include("referral.urls", namespace="referral")),
    path('destination/', include("destination.urls", namespace="destination")),
    path('cart/', include("pay.urls", namespace="pay")),
    path('genie/', include("genie.urls", namespace="genie")),
    path('reviews/', include("reviews.urls", namespace="reviews")),
    path('django-rq/', include('django_rq.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)