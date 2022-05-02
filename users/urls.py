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
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("", views.index, name='index'),
    path("upload", views.upload_image, name='upload_image'),
    path("list", views.image_list, name='image_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)