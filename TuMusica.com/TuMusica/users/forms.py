"""Users forms."""
# Django
from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    """Sign up new user form."""

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        """Validate that the email doesn't exist in the database."""
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("This email already exists.")

        return data
