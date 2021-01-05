from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse
from django.db.models import Q
from account.models import User
from .forms import PostCreationForm, CommentCreationForm, SearchPostsForm
from .models import Post, Comment




# BASIC
def home(request):
    """ Domovská stránka"""

    if not request.user.is_authenticated:
        return redirect("blog-welcome")
    
    posts_count = Post.objects.all().count()
    users_count = User.objects.all().count()
    comments_count = Comment.objects.all().count()

    context = {
        "title": "Home",
        "posts_count": posts_count,
        "users_count": users_count,
        "comments_count": comments_count,
    }


    return render(request, "blog/home.html", context=context)
    
        

def welcome(request):
    """ Úvodná stránka """

    return render(request, "blog/welcome.html")


# POSTS
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
    found_posts = Post.objects.filter(Q(title__contains=post_search) | Q(author__username__contains=post_search)).order_by(order)
    count = found_posts.count()
    context = {
        "posts": found_posts,
        "form": form,
        "title": "Search",
        "count": count,
    }
    return render(request, "blog/browse.html", context=context)


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

    context = {
        "form": form,
        "title": "New Post",
    }
    return render(request, "blog/posts/post_add.html", context=context)


def post_view(request, pk):
    """ Zobrazenie konkrétneho príspevku """
    
    found_post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=found_post).order_by("-date")

    #formulár pre komentár
    if request.method == "POST":
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():
            created_comment = comment_form.save(commit=False)
            created_comment.author = request.user
            created_comment.post = found_post
            created_comment.save()

            return redirect(request.path)
    else:
        comment_form = CommentCreationForm()

    context = {
        "post": found_post,
        "comments": comments,
        "form": comment_form,
        "comments_count": comments.count(),
        "title": found_post.title,
    }

    return render(request, "blog/posts/post_view.html", context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """ Upravenie daného príspevku """

    model = Post
    fields = ["title","content"]
    template_name = "blog/posts/post_edit.html"
    success_message = "%(title)s was edited."

    def form_valid(self, form):
        """ Nastaví prihláseného užívateľa ako autora príspevku """

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Funkcia, ktorá overí či prihlásený užívateľ je autorom príspevku """

        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """ Vymazanie daného príspevku """

    model = Post
    success_url = "/"
    template_name = "blog/posts/post_confirm_delete.html"
    success_message = "%(title)s was removed."

    def test_func(self):
        """ Funkcia, ktorá overí či prihlásený užívateľ je autorom príspevku """

        post = self.get_object()
        return self.request.user == post.author



# COMMENTS
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """ Úprava komentára """

    model = Comment
    fields = ["content"]
    template_name = "blog/comments/comment_edit.html"
    success_message = "Your comment was edited."

    def form_valid(self, form):
        """ Nastaví prihláseného užívateľa ako autora komentára """

        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """ Funkcia, ktorá overí či prihlásený užívateľ je autorom komentára """

        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """ Funkcia, ktorá určí kam má byť užívateľ presmerovaný po vymazaní komentára """

        return reverse("blog-post-view", kwargs={"pk" : self.get_object().post.id })


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """ Vymazanie komentára """

    model = Comment
    template_name = "blog/comments/comment_confirm_delete.html"
    success_message = "Your comment was removed."

    def test_func(self):
        """ Funkcia, ktorá overí či prihlásený užívateľ je autorom komentára """

        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """ Funkcia, ktorá určí kam má byť užívateľ presmerovaný po vymazaní komentára """

        return reverse("blog-post-view", kwargs={"pk" : self.get_object().post.id })