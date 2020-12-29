from django import forms
from .models import Post, Comment


class PostCreationForm(forms.ModelForm):
    """ Formulár pre vytvorenie nového príspevku """

    class Meta:
        """ Vnorená trieda pre konfiguráciu """

        model = Post
        fields = ["title", "content"]

class CommentCreationForm(forms.ModelForm):
    """ Formulár pre vytvorenie nového komentára k danému príspevku """

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 1, 'placeholder':'Write a comment here...','class':'form-control'}),
        }


