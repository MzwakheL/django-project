from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """
    Form for user login.

    Inherits from Django's AuthenticationForm and adds placeholder attributes and CSS classes to the fields.

    Fields:
        - username: CharField for the username.
        - password: CharField for the password.

    Widgets:
        - username: TextInput widget with placeholder and CSS classes.
        - password: TextInput widget with placeholder and CSS classes.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

class SignupForm(UserCreationForm):
    """
    Form for user signup.

    Inherits from Django's UserCreationForm and adds placeholder attributes and CSS classes to the fields.

    Meta:
        model: The User model.
        fields: The fields to include in the form.

    Fields:
        - username: CharField for the username.
        - email: CharField for the email address.
        - password1: CharField for the password.
        - password2: CharField for password confirmation.

    Widgets:
        - username: TextInput widget with placeholder and CSS classes.
        - email: TextInput widget with placeholder and CSS classes.
        - password1: TextInput widget with placeholder and CSS classes.
        - password2: TextInput widget with placeholder and CSS classes.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        email = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your email address',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password1 = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password2 = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))