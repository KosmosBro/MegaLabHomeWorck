from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """ Форма для входа в систему. """
    phone_number = forms.IntegerField(label='Phone number', label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Password', label_suffix='')


class RegisterForm(UserCreationForm):
    phone_number = forms.IntegerField(label='Phone number', label_suffix='')
    password1 = forms.CharField(widget=forms.PasswordInput, required=False, label='Password', label_suffix='')
    password2 = forms.CharField(widget=forms.PasswordInput, required=False, label='Repeat Password', label_suffix='')

    class Meta:
        model = User
        fields = ('username', 'password')
