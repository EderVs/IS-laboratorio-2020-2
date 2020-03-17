"""Users views."""
# Django
from django.shortcuts import render
from django.views import View

# Forms
from users.forms import SignUpForm


class SignUp(View):
    """New User Sign Up."""

    template = "users/signup.html"

    def get(self, request):
        """Render sign up form."""
        return render(request, self.template)
