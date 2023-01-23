from django.contrib.auth.forms import  AuthenticationForm
from django import forms

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')