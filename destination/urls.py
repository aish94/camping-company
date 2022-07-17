from django.urls import path
from destination.views import (destination, destination_detail_page,
                               circuits, circuit, success, camp_add,
                               camp_update, experiences, experience_detail,
                               experience_success)

app_name = "destination"

urlpatterns = [
    path('', destination, name="destinations"),
    path('experiences/', experiences, name="experiences"),
    path('circuits/', circuits, name="circuits"),
    path('success/', success, name="success"),
    path('experiences/booked/', experience_success, name="experience_success"),
    path('camp-add/', camp_add, name="camp_add"),
    path('experiences/<slug:slug>/', experience_detail, name="experience_detail"),
    path('<slug:slug>/update/', camp_update, name="camp_update"),
    path('<slug:slug>/', destination_detail_page, name="destination_detail_page"),
    path('circuits/<slug:slug>/', circuit, name="circuit"),
]