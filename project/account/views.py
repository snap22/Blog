from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


from .forms import AccountCreationForm, AccountUpdateForm, ProfileUpdateForm



def register(request):
    """ Registrácia užívateľa """
    
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()     # ulozi uzivatela do databazy a zaroven hashne jeho heslo
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, f"Account was created successfully.")
            return redirect("blog-home")
    else:
        form = AccountCreationForm()
    return render(request, "account/register.html", {"form": form})


@login_required
def profile(request):
    """ Profil užívateľa """

    if request.method == "POST":
        user_form = AccountUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect("account-profile")

    else:
        user_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form" : user_form,
        "profile_form" : profile_form,
        "title" : request.user.username,
    }

    return render(request, "account/profile.html", context)


