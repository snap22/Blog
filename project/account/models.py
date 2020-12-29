from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """ Trieda, ktorá je rozšírením pre účet používateľa """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default="default.png", upload_to="profile_pictures")
    

    def save(self, *args, **kwargs):
        """ Override pre uloženie - uloží obrázok vo vhodnej forme """

        super().save(*args, **kwargs)
        
        image = Image.open(self.picture.path)
        
        if image.height > 300 or image.width > 300:
            image.thumbnail((300,300))
            image.save(self.picture.path)

    def __str__(self):
        return f"Profile for { self.user.username }"


