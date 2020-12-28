from django import forms
from .models import Post, Comment


class PostCreationForm(forms.ModelForm):
    """ Formulár pre vytvorenie nového príspevku """

    class Meta:
        """ Vnorená trieda pre konfiguráciu """

        model = Post
        fields = ["title", "content"]

