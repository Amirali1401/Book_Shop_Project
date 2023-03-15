from django import forms

from django.contrib.auth.models import User

from .models import ChangePassword
from django.contrib.auth.forms import PasswordChangeForm

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name' , 'email' , 'password' , ]

