from django import forms
from .models import Post, Comment, ContactMessage


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


class ContactForm(forms.ModelForm):
    """ Formulár pre kontaktovanie """

    class Meta:
        model = ContactMessage
        fields = ["title", "sender_name", "sender_email", "help_type", "content"]
        labels = {
            "sender_name": "Your name",
            "sender_email": "Your email",
            "help_type": "How can we help you?",
        }


class SearchPostsForm(forms.Form):
    """ Formulár na vyhľadávanie príspevkov """

    search = forms.CharField(label="Search by", required=False, max_length=100, widget=forms.TextInput(attrs={'name': 'search','placeholder':'Search for the author or the title'}))
    order_by = forms.ChoiceField(label="Search by the most recent", choices=(("new","Most Recent"), ("old","Oldest")))

