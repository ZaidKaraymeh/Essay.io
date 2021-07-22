from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import ProfileUpdateForm, RegisterForm, UserUpdateForm, UserCreationForm



# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You are now able to log in ")
            return redirect("login")
    else:

        form = RegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)


# add LOGIN_URL = "URL-NAME" in settings.py
@login_required
def profile(request):
    if request.method == "POST":

        # instance = request.user gives form current user logged in
        userUpdateForm = UserUpdateForm( request.POST,  instance=request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request, "Your profile has been updated")
            return redirect('profile')
    else:
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)

    context = {"userUpdateForm": userUpdateForm, "profileUpdateForm": profileUpdateForm}
    return render(request, "users/profile.html", context )

