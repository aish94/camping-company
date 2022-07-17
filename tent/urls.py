from django.urls import path
from tent.views import (tent_create_check,
                        tent_update_check,
                        tents, payment_failure,
                        payment_success, cart,
                        tent_info)

app_name = "tent_check"

urlpatterns = [
    path('all/', tents, name="all"),
    path('success/', payment_success, name="success"),
    path('failure/', payment_failure, name="failure"),
    path('cart/<slug:slug>/', cart, name="cart"),
    path('tent_info/<slug:slug>/', tent_info, name="tent_info"),
    path('<int:pk>/create/', tent_create_check, name="tent_create_check"),
    path('<int:pk>/update/', tent_update_check, name="tent_update_check"),
]