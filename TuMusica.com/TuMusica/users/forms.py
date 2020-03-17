"""Users forms."""
# Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class SignUpForm(forms.Form):
    """Sign up new user form."""

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        """Validate that the email doesn't exist in the database.

        Just validating email field.
        """
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("This email already exists.")

        return data


class LoginForm(AuthenticationForm):
    """Login form."""

    def clean(self):
        """Validate data.

        Validating all fields.
        """
        username = self.data["username"]
        password = self.data["password"]

        if User.objects.filter(username=username).count() == 0:
            self.add_error(
                "username", forms.ValidationError("This email does not exists.")
            )

        # authenticate search for the user with that username and password.
        # authenticate do not log any user.
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error("password", forms.ValidationError("Wrong password."))
