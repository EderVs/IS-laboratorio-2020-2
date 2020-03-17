"""Users views."""
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Forms
from users.forms import SignUpForm, LoginForm


class SignUp(View):
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

        new_user = User.objects.create_user(
            username=form.cleaned_data["email"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        return HttpResponse("<h1>User Created!</h1>")


class Login(View):
    """New User Sign Up."""

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
        login(request, user)

        return HttpResponse("<h1>User logged!</h1>")
