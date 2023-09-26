from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #subclass that tells django it is the User model we are modifying
        model = User
        # define the field names and the order they should be displayed
        fields = ['username', 'email', 'password1', 'password2']