from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from project.settings_custom import DEFAULT_PICTURE, DEFAULT_PICTURE_URL, PROFILE_PICTURES_LOCATION
import os


class Profile(models.Model):
    """ Trieda, ktorá je rozšírením pre účet používateľa """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default=DEFAULT_PICTURE, upload_to=PROFILE_PICTURES_LOCATION)
    info = models.TextField(default="No info was provided", blank=True, null=True)
    
    def __str__(self):
        return f"Profile for { self.user.username }"
        
    # def get_picture(self):
    #     """ Metóda pre bezpečné získanie obrázka používateľa """

    #     if os.path.exists(self.picture.path):
    #         return self.picture.url
    #     return DEFAULT_PICTURE_URL

    # nie je potrebna tato metoda lebo pillow nefunguje dobre s AWS
    # def save(self, *args, **kwargs):
    #     """ Override pre uloženie - uloží obrázok vo vhodnej forme """

    #     super().save(*args, **kwargs)

    #     try:
    #         image = Image.open(self.picture.path)
            
    #         if image.height > 300 or image.width > 300:
    #             image.thumbnail((300,300))
    #             image.save(self.picture.path)

    #     except FileNotFoundError:   
    #         pass




