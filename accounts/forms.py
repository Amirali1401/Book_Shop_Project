from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import user_passes_test


def email_check(user):
   return  user.email.endswith("@example.com")


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name' , 'last_name' , 'email']



class ChangePasswordForm(forms.Form):
    new_password1 = forms.CharField(max_length=15 , required = True , widget = forms.PasswordInput)
    new_password12 = forms.CharField(max_length=15 , required = True , widget = forms.PasswordInput)