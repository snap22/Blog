from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.http import request
from django.urls import reverse



class Post(models.Model):
    """ Trieda predstavujúca model pre príspevok """

    title = models.CharField(max_length = 100)
    content = tinymce_models.HTMLField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: [{self.title}] by {self.author.username}"

    def get_absolute_url(self):
        return reverse("blog-post-view", kwargs={"pk" : self.pk})
    

class Comment(models.Model):
    """ Trieda predstavujúca model pre komentár k danému príspevku """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment to: [{self.post.title}] by {self.author.username}"


class ContactMessage(models.Model):
    """ Model pre kontaktnú správu """

    CHOICES = (
        ("","Choose a type..."),
        ("0","Report an issue"),
        ("1","Report a post"),
        ("2","Feedback"),
        ("3","Support"),
        ("4","Other"),
    )

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    sender_name = models.CharField(max_length=150)
    sender_email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)
    help_type = models.CharField(choices=CHOICES, max_length=1)

    def __str__(self):
        return f"Contact message '{self.title}' by {self.sender_name}"
