from django.urls import path
from pay.views import (cart, payment_success, payment_failure)

app_name = "pay"

urlpatterns = [
    path('', cart, name="pay"),
    path('success/', payment_success, name="success"),
    path('failure/', payment_failure, name="failure"),
]