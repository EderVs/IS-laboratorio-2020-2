"""Users forms."""
# Django
from django import forms


class SignUpForm(forms.Form):
    """Sign up new user form."""

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.PasswordInput()
