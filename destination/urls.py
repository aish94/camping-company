from django.conf.urls import url
from destination.views import (destination, destination_detail_page,
                               circuits, circuit, success, camp_add,
                               camp_update, experiences, experience_detail,
                               experience_success)

app_name = "destination"

urlpatterns = [
    url(r'^$', destination, name="destinations"),
    url(r'^experiences/$', experiences, name="experiences"),
    url(r'circuits/$', circuits, name="circuits"),
    url(r'success/$', success, name="success"),
    url(r'experiences/booked/$', experience_success, name="experience_success"),
    url(r'camp-add/$', camp_add, name="camp_add"),
    url(r'experiences/(?P<slug>[\w-]+)/$', experience_detail, name="experience_detail"),
    url(r'(?P<slug>[\w-]+)/update/$', camp_update, name="camp_update"),
    url(r'^(?P<slug>[\w-]+)/$', destination_detail_page, name="destination_detail_page"),
    url(r'^circuits/(?P<slug>[\w-]+)/$', circuit, name="circuit"),
]