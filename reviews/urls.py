from django.conf.urls import url
from . import views
app_name= 'reviews'

urlpatterns = [
    # ex: /
    url(r'^$', views.review, name='review'),
    #url(r'^Create$', views.Create, name='Create'),
    url(r'^Show$', views.Show, name='Show'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^review_list$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^reviewdetail/(?P<pk>\d+)/$', views.review_detail, name='review_detail'),
    # ex: /destination/
    url(r'^destination$', views.destination_list, name='Campsite_list'),
    # ex: /destination/5/
    url(r'^Camp/(?P<pk>\d+)/$', views.destination_detail, name='destination_detail'),

]
