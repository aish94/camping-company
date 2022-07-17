from django.urls import path
from trip.views import trip_create, trip_update

app_name = "trip"

urlpatterns = [
    path('<int:pk>/create/', trip_create, name="create_trip"),
    path('<int:pk>update/', trip_update, name="update_trip"),

]
