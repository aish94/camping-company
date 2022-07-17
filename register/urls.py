from django.urls import path
from register.views import (signup, signin, sign_out,
                            welcome, pass_reset,pass_rediretor)


app_name = "register"

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', signin, name="signin"),
    path('logout/', sign_out, name="signout"),
    path('welcome/', welcome, name="welcome"),
    path('reset/<slug:slug>/', pass_rediretor, name="pass_rediretor"),
    path('reset/', pass_reset, name="pass_reset"),

]
