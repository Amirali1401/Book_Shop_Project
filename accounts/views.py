from django.shortcuts import render , redirect
from django.contrib.auth.models import User

from  .forms import RegisterForm
# Create your views here.


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        User.objects.create_user(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
        )

        return redirect('login')
    return render(request , 'accounts/register.html' , context={'form':form})