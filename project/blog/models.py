from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    """ Trieda predstavujúca model pre príspevok """

    title = models.CharField(max_length = 100)
    content = HTMLField()
    date = models.DateTimeField(timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: [{self.title}] by {self.author.username}"
    

class Comment(models.Model):
    """ Trieda predstavujúca model pre komentár k danému príspevku """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Comment to: [{self.post.title}] by {self.author.username}"