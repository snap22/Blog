from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .forms import AccountCreationForm, AccountUpdateForm, ProfileUpdateForm
from .models import User
from blog.models import Post, Comment



def register(request):
    """ Registrácia užívateľa """
    
    if request.user.is_authenticated:
        return redirect("blog-home")

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
    return render(request, "account/register.html", {"form": form, "title":"Register"})


def profile_inspect(request, pk):
    """ Zobrazenie profilu ľubovoľného užívateľa """

    found_user = get_object_or_404(User, pk=pk)
    created_posts = Post.objects.filter(author=found_user).all()
    created_comments = Comment.objects.filter(author=found_user).all()

    context = {
        "title": found_user.username,
        "posts_count": created_posts.count(),
        "comments_count": created_comments.count(),
        "found_user": found_user,
    }

    return render(request, "account/inspect.html", context=context)


#Possible Exception: RelatedObjectDoesNotExist
@login_required
def profile(request):
    """ Profil prihláseného užívateľa """
    
    if request.method == "POST":
        user_form = AccountUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect("account-profile")
        else:
            messages.error(request, "Error! Couldn't update your account.")

    else:
        user_form = AccountUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form" : user_form,
        "profile_form" : profile_form,
        "title" : request.user.username,
    }

    return render(request, "account/profile.html", context)


