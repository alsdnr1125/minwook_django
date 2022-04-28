from django.urls import path
from . import views
from .models import User
from django.conf.urls.static import static
from django.conf import settings
from.views import return_user
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    #path("", views.index, name='index'),
]
