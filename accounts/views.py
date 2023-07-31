from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm , PasswordChangeForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test


from  .forms import RegisterForm , UserForm , PasswordChangeForm
from order.models import Order
from books.models import Wishlist
from notification.models import Notification


# Create your views here.


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )

        return redirect('login')
    return render(request, 'accounts/register.html', context={'form': form})


@login_required()
def change_account_view(request):
    form = UserForm(request.POST or None, instance=request.user)
    password_form = PasswordChangeForm(user=request.user, data=request.POST)
    wishlist_books = Wishlist.objects.all()
    notifications = Notification.objects.filter(user = request.user , read=False).order_by('id')

    if form.is_valid() and password_form.is_valid():
        form.save()
        password_form.save()

    return render(request, 'accounts/my_account.html', context={'form': form , 'password_form':password_form , 'wishlist_books' : wishlist_books , 'notifications':notifications  })



def change_password(request):
      user = User.objects.get(username = 'amirali')
      user.set_password('a123')
      user.save()
      return HttpResponse('Your password was changed')