from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from account.models import User
from blog.forms import SearchPostsForm
from blog.models import Post, Comment



def home(request):
    """ Domovská stránka"""

    posts_count = Post.objects.all().count()
    users_count = User.objects.all().count()
    comments_count = Comment.objects.all().count()

    context = {
        "title": "Home",
        "posts_count": posts_count,
        "users_count": users_count,
        "comments_count": comments_count,
    }

    return render(request, "blog/main/home.html", context=context)
    
        
def welcome(request):
    """ Úvodná stránka """

    return render(request, "blog/main/welcome.html")


def about(request):
    """ Informácie ohľadom stránky """

    return render(request, "blog/main/about.html")


def contacts(request):
    """ Stránka s kontaktnými informáciami """

    return render(request, "blog/main/contacts.html")


def browse_posts(request):
    """ Vyhlľadávanie príspevkov na základe zadaného slova """

    post_search = request.GET.get("search")
    post_order = request.GET.get("order_by")

    order = "date" if post_order == "old" else "-date"

    default_form_values = {
        "search": post_search,
    }

    if post_search == None:
        post_search = ""
    
    form = SearchPostsForm(initial=default_form_values)
    filtered_posts = Post.objects.filter(Q(title__contains=post_search) | Q(author__username__contains=post_search)).order_by(order)
    posts_count = filtered_posts.count()

    posts_per_page = 4

    paginator = Paginator(filtered_posts, posts_per_page)
    page_number = request.GET.get("page")
    found_posts = paginator.get_page(page_number)

    context = {
        "posts": found_posts,
        "form": form,
        "title": "Search",
        "count": posts_count,
    }
    return render(request, "blog/main/browse.html", context=context)
