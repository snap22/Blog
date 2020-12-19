from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Domovská stránka

    if request.user.is_authenticated:
        return render(request, "blog/home.html")
    else:
        return redirect("blog-welcome")

def welcome(request):
    # Uvodna stranka

    return render(request, "blog/welcome.html")