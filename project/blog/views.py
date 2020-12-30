from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from .forms import PostCreationForm, CommentCreationForm
from .models import Post, Comment

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