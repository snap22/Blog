from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from .forms import AccountCreationForm



def register(request):
    """ Registrácia užívateľa """
    
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()     # hodi uzivatela do databazy, a hashne heslo
            messages.success(request, f"Account was created successfully.")
            return redirect("blog-home")
    else:
        form = AccountCreationForm()
    return render(request, "account/register.html", {"form": form})



def login_view(request):
    """ Prihlásenie užívateľa """

    pass



@login_required
def logout_view(request):
    """ Odhlásenie užívateľa """

    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("blog-welcome")
