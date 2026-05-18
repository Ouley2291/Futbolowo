from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "placeholder": 'Your username',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))

    email = forms.CharField(label="E-mail", widget=forms.EmailInput(attrs={
        "placeholder": 'Your email adress',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'Your password',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))

    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'Repeat password',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "placeholder": 'Your username',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'Your password',
        "class": 'w-full p-2 rounded-xl text-gray-900'
    }))    