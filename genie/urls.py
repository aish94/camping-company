from django.conf.urls import url
from genie.views import create, index, show, offline

app_name = "genie"

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^offline/$', offline, name="offline"),
    url(r'^(?P<pk>\d+)/create$', create, name="create"),
    url(r'^(?P<pk>\d+)/show$', show, name="show"),
]
