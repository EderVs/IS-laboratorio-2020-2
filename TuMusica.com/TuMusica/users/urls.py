"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from users import views

app_name = "users"
urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
