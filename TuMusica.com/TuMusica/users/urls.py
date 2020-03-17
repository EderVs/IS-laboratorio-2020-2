"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from users import views

app_name = "users"
urlpatterns = [
    path("sign-up/", views.SignUp.as_view(), name="sign_up"),
    path("login/", views.Login.as_view(), name="login"),
]
