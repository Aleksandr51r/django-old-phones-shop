from .models import User, ShopProfile
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)


class LoginUser(AuthenticationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',
                  'role', 'phone_number']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        #     'email': forms.EmailField(attrs={'class': 'form-input'}),
        # }
        # labels = {'first_name': 'Url'}


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration__input', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration__input', 'placeholder': 'Enter last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration__input', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'registration__input', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registration__input', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registration__input', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'registration__input', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'registration__input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')