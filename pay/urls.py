from django.urls import path
from genie.views import create, index, show, offline

app_name = "genie"

urlpatterns = [
    path('', index, name="index"),
    path('offline/', offline, name="offline"),
    path('<int:pk>/create/', create, name="create"),
    path('<int:pk>/show/', show, name="show"),
]
