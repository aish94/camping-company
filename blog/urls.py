from django.conf.urls import url
from blog.views import (all_blog, blog_detail,
                        event, event_form)

app_name = "blog"

urlpatterns = [
    url(r'^$', all_blog, name="all_blog"),
    url(r'^event/$', event, name="event"),
    url(r'^event-form/$', event_form, name="event_form"),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name="blog_detail"),

]
