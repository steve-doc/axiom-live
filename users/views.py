from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# user registration view
def register(request):
    if request.method == 'POST':  # checks if POST has been received from register.html
        # assigns form data to form object
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # is_valid method checks if form data fields are valid
            form.save()  # saves form to user database
            # is_valid form data is stored in form.cleaned_data dictionary
            # assigns stored username to variable
            username = form.cleaned_data.get('username')
            # next create success message by injecting username into f string
            messages.success(
                request, f'Your account has been created! You are now able to login.')
            return redirect('login')  # redirects to login page
    else:
        form = UserRegisterForm()  # asssigns blank UserCreation form to form object
    return render(request, 'users/register.html', {'form': form})


# user profile view
@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)
