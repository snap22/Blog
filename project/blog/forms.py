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


class SearchPostsForm(forms.Form):
    """ Formulár na vyhľadávanie príspevkov """

    title = forms.CharField(label="Title of the post", required=False, max_length=100, widget=forms.TextInput(attrs={'name': 'title', 'placeholder':'Search for the title'}))
    author = forms.CharField(label="Author of the post", required=False, max_length=100, widget=forms.TextInput(attrs={'name': 'author','placeholder':'Search for the author'}))


