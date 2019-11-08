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
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include("app.urls", namespace="app")),
    url(r'^equipment/', include("equipment.urls", namespace="equipment")),
    url(r'^tent/', include("tent.urls", namespace="tent")),
    url(r'^trip/', include("trip.urls", namespace="trip")),
    url(r'^vehicles/', include("vehicle.urls", namespace="vehicle")),
    url(r'^accounts/', include("register.urls", namespace="register")),
    url(r'^user/', include("customer.urls", namespace="customer")),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^referral/', include("referral.urls", namespace="referral")),
    url(r'^destination/', include("destination.urls", namespace="destination")),
    url(r'^cart/', include("pay.urls", namespace="pay")),
    url(r'^genie/', include("genie.urls", namespace="genie")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)