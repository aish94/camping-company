from django.urls import path
from referral.views import referred_view


app_name = "referral"

urlpatterns = [
    path('<slug:slug>/', referred_view, name="referred"),
]
