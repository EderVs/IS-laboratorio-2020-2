"""Users views."""
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import ExtendedUser

# Forms
from users.forms import SignUpForm, LoginForm


class SignUpView(View):
    """New User Sign Up."""

    template = "users/signup.html"

    def get(self, request):
        """Render sign up form."""
        form = SignUpForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = SignUpForm(request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = User.objects.create_user(
            username=form.cleaned_data["email"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        ExtendedUser.objects.create(user=user)
        return redirect("users:login")


class LoginView(View):
    """User Login."""

    template = "users/login.html"

    def get(self, request):
        """Render sign up form."""
        form = LoginForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        # As simple as telling django the user to login.
        login(request, user)

        return redirect("music:home")


class LogoutView(View):
    """Logout View."""

    def get(self, request):
        """Logout logged user."""
        # As simple as.
        logout(request)
        return redirect("music:home")


class ProfileView(LoginRequiredMixin, View):
    """Profile View."""

    template = "users/profile.html"

    def get(self, request):
        """Display profile template."""
        context = {"songs": request.user.extended_user.fav_songs.all()}
        return render(request, self.template, context)
