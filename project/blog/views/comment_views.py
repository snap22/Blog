from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse
from blog.models import Post, Comment



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