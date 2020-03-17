"""Users views."""
# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Forms
from users.forms import SignUpForm


class SignUp(View):
    """New User Sign Up."""

    template = "users/signup.html"

    def get(self, request):
        """Render sign up form."""
        return render(request, self.template)

    def post(self, request):
        """Receive and validate sign up form."""
        form = SignUpForm(request.POST)
        context = {}
        if not form.is_valid():
            context["form"] = form
            return render(request, self.template, context)
        return HttpResponse("<h1>Valid!</h1>")
