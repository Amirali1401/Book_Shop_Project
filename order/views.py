from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from .models import Order  ,OrderItem
from cart.cart import Cart
from .forms import OrderForm

# Create your views here.

@login_required()
def order_create(request):
    form =  OrderForm(request.POST)
    cart = Cart(request)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user = request.user
        form_obj.save()
        for item in cart:
            quantity = item['quantity']
            book = item['book_obj']
            OrderItem.objects.create(
                order = form_obj,
                book = book,
                quantity = quantity,
                price = book.price,
            )

            cart.clear()
            request.user.first_name = form_obj.first_name
            request.user.last_name = form_obj.last_name
            request.session['order_id']  = form_obj.id
            return redirect('payment:payment_process')

    return render(request , 'order/order_create.html' , context={'form':form})


