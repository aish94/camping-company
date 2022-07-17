from django.urls import path
from blog.views import (all_blog, blog_detail,
                        event, event_form, event_pay,
                        payment_success, payment_failure)

app_name = "blog"

urlpatterns = [
    path('', all_blog, name="all_blog"),
    path('event/', event, name="event"),
    path('event_pay/', event_pay, name="pay"),
    path('success/', payment_success, name="success"),
    path('failure/', payment_failure, name="failure"),
    path('event-form/', event_form, name="event_form"),
    path('<slug:slug>/', blog_detail, name="blog_detail"),
]
