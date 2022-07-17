from django.urls import path
from reviews.views import destination_add_review, blog_add_review

app_name = "reviews"

urlpatterns = [
    path('review_destination/', destination_add_review, name="reviews_destination"),
    path('review_blog/', blog_add_review, name="reviews_blog"),
]