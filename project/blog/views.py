from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
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

    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            created_post = form.save(commit=False)
            created_post.author = request.user
            created_post.save()

            messages.success(request,"Post creation was successful.")
            return redirect("blog-home")
    else:
        form = PostCreationForm()
    return render(request, "blog/posts/post_add.html", {"form": form})