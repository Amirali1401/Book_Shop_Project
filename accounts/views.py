from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required

from  .forms import RegisterForm , UserForm
# from order.models import Order
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
def my_account(request):
    wishlist_books = Wishlist.objects.all()
    # order_books = Order.objects.all()
    return render(request , 'accounts/my_account.html' , context={'wishlist_books':wishlist_books , 'order_books':order_books})

#
# def change_account_form(request ,user_id):
#     form = UserForm(request.POST)
#     user= User.objects.get(id = user_id)
