from django.contrib import admin
from .models import Post, Comment, ContactMessage

# Registrácia modelu aby ho bolo vidno v /admin 
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ContactMessage)