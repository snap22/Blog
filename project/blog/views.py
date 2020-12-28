from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm

# Create your views here.

def home(request):
    """ Domovská stránka"""

    if request.user.is_authenticated:
        return render(request, "blog/home.html")
    else:
        return redirect("blog-welcome")

def welcome(request):
    """ Úvodná stránka """

    return render(request, "blog/welcome.html")


@login_required
def post_new(request):
    """ Tvorba nového príspevku """

    form = PostCreationForm()
    return render(request, "blog/posts/post_add.html", {"form": form})