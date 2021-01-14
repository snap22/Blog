from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class AccountCreationForm(UserCreationForm):
    """ Formulár pre vytvorenie novéo užívateľa, ktorý dedí z django formulára pre užívateľa"""

    email = forms.EmailField()

    class Meta:
        """ Vnorená trieda pre konfiguráciu """

        model = User
        fields = ["username","email","password1","password2"]


class AccountUpdateForm(forms.ModelForm):
    """ Formulár pre aktualizáciu údajov o uzívateľovi """

    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() and self.instance.username != username:
            raise forms.ValidationError(f"{username} is already in use.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists() and self.instance.email != email:
            raise forms.ValidationError(f"{email} is already in use.")
        return email

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """ Formulár pre aktualizáciu údajov o profile uzívateľa """

    class Meta:
        model = Profile
        fields = ["picture", "info"]


class AccountDeleteForm(forms.Form):
    """ Formulár pre potvrdenie vymazania účtu """

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AccountDeleteForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        user = self.request.user
        password = self.cleaned_data["password"]
        if not user.check_password(password):
            raise forms.ValidationError("The password is incorrect.")
        return password
            


