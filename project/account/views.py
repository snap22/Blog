from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


from .forms import AccountCreationForm



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

