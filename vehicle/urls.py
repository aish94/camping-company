from django.urls import path
from vehicle.views import (vehicles, vehicle_create_check,
                           vehicle_update_check, vehicle_info,vehicle)

app_name = "vehicles"

urlpatterns = [
    path('', vehicles, name="vehicles"),
    path('<int:pk>/create/', vehicle_create_check, name="vehicle_create_check"),
    path('<int:pk>/update/', vehicle_update_check, name="vehicle_update_check"),
    path('vehicle_info/', vehicle_info, name="vehicle_info"),
    path('all/', vehicle, name="vehicle"),
]
