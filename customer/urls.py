from django.conf.urls import url
from customer.views import (user_page, book,
                            custom_itinerary,
                            create_itinerary,
                            delete_itinerary,
                            trip_detail,
                            form, experience)

app_name = "customer"

urlpatterns = [
    url(r'^$', user_page, name="user_page"),
    url(r'^create/$', create_itinerary, name="create_itinerary"),
    url(r'^book/(?P<pk>\d+)/success/$', book, name="book"),
    url(r'^itinerary/delete/$', delete_itinerary, name="delete_itinerary"),
    url(r'^itinerary/$', custom_itinerary, name="custom_itinerary"),
    url(r'^trip_detail/$', trip_detail, name="trip_detail"),
    url(r'^form/$', form, name="form"),
    url(r'^experience/$', experience, name="form"),

]
