from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    """
    Form to log the user in
    """

    #class Meta:
    #    model = User
    #    fields = ["username", "password"]
    username = forms.CharField()
    password = forms.CharField()
