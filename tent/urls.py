from django.conf.urls import url
from tent.views import (tent_create_check,
                        tent_update_check,
                        tents, payment_failure,
                        payment_success, cart,
                        tent_info)

app_name = "tent_check"

urlpatterns = [
    url(r'^all/$', tents, name="all"),
    url(r'^success/$', payment_success, name="success"),
    url(r'^failure/$', payment_failure, name="failure"),
    url(r'^cart/(?P<slug>[\w-]+)/$', cart, name="cart"),
    url(r'^tent_info/(?P<slug>[\w-]+)/$', tent_info, name="tent_info"),
    url(r'^(?P<pk>\d+)/create/$', tent_create_check, name="tent_create_check"),
    url(r'^(?P<pk>\d+)/update/$', tent_update_check, name="tent_update_check"),
]