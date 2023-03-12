from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from  .forms import RegisterForm , UserForm
from order.models import Order
from books.models import Wishlist
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



@login_required()
def change_account_view(request , user_id):
    user = get_object_or_404(User , id = user_id)
    form = UserForm( request.POST , instance=user )
    if form.is_valid():
        form.save()


    return render(request , 'accounts/my_account.html' , context={'form':form ,'user':user })



@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })


