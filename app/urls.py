from django.urls import path
from app import views

app_name = "app"

urlpatterns = [
    path('', views.home, name="home"),
    path('all-user/', views.all_user, name="all_user"),
    path('detail-user/<int:pk>/', views.detail_user, name="detail_user"),
    path('findus/', views.findus, name="findus"),
    path('represent/', views.represent, name="represent"),
    path('calender/', views.calender, name="calender"),
    path('status/<int:pk>/show/', views.show_status, name="show_status"),
    path('terms-condition/', views.terms_condition, name="terms_condition"),
    path('faq/', views.faq, name="faq"),
    path('damage-charges/', views.damage_charges, name="damage_charges"),
    path('sitemap/', views.sitemap, name="sitemap"),
]