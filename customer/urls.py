from django.urls import path
from customer.views import (user_page, book,
                            custom_itinerary,
                            create_itinerary,
                            delete_itinerary,
                            trip_detail,
                            form, experience,
                            filter_sites)

app_name = "customer"

urlpatterns = [
    path('', user_page, name="user_page"),
    path('create/', create_itinerary, name="create_itinerary"),
    path('book/<int:pk>/success/', book, name="book"),
    path('itinerary/delete/', delete_itinerary, name="delete_itinerary"),
    path('itinerary/', custom_itinerary, name="custom_itinerary"),
    path('trip_detail/', trip_detail, name="trip_detail"),
    path('form/', form, name="form"),
    path('experience/', experience, name="experience"),
    path('filter_sites/', filter_sites, name="filter_sites"),
]
