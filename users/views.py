from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST': #checks if POST has been received from register.html
        form = UserRegisterForm(request.POST) #assigns form data to form object
        if form.is_valid(): #is_valid method checks if form data fields are valid
            form.save() #saves form to user database
            #is_valid form data is stored in form.cleaned_data dictionary
            username = form.cleaned_data.get('username') #assigns stored username to variable
            #next create success message by injecting username into f string
            messages.success(request, f'Your account has been created! You are now able to login.') 
            return redirect('login') #redirects to login page
    else:
        form = UserRegisterForm() #asssigns blank UserCreation form to form object
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render (request, 'users/profile.html')