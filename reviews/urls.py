from django.conf.urls import url
from reviews.views import destination_add_review

app_name = "reviews"

urlpatterns = [
    # url(r'^$', cart, name="pay"),
    url(r'^review_destination/$', destination_add_review, name="reviews_destination"),
    # url(r'^failure/$', payment_failure, name="failure"),
]