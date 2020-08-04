from django.conf.urls import url
from blog.views import (all_blog, blog_detail,
                        event, event_form, event_pay,
                        payment_success, payment_failure)

app_name = "blog"

urlpatterns = [
    url(r'^$', all_blog, name="all_blog"),
    url(r'^event/$', event, name="event"),
    url(r'^event_pay/$', event_pay, name="pay"),
    url(r'^success/$', payment_success, name="success"),
    url(r'^failure/$', payment_failure, name="failure"),
    url(r'^event-form/$', event_form, name="event_form"),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name="blog_detail"),
]
