from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AccountCreationForm

def register(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()     # hodi uzivatela do databazy, a hashne heslo
            messages.success(request, f"Account was created successfully.")
            return redirect("blog-home")
    else:
        form = AccountCreationForm()
    return render(request, "account/register.html", {"form": form})
