from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# define form for user registration page
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # subclass that tells django it is the User model we are modifying
    class Meta:
        model = User
        # define the field names and the order they should be displayed
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2']


# define 2 forms to update user profile. 2nd form captures image file
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # subclass that tells django it is the User model we are modifying
    class Meta:
        model = User
        # define the field names and the order they should be displayed
        fields = ['first_name', 'last_name', 'username', 'email']


# image file form combines with UserUpdateFrom
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
