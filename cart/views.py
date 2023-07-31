from django.shortcuts import render , redirect, get_object_or_404

from .cart import Cart
from .forms import AddToBooktCartForm
from books.models import Book

# Create your views here.

   #show detail and make explain about my cart
def detail_cart_view(request):

     cart = Cart(request)

     for item in cart:
         item['update_quantity_cart'] = AddToBooktCartForm(initial={'quantity':item['quantity'] , 'inplace':True})

     return render(request , 'cart/detail_view_cart.html' , context={'cart':cart})




def add_to_cart(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    form = AddToBooktCartForm(request.POST)
    cart = Cart(request)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        inplace = cleaned_data['inplace']              #add your product in your cart
        cart.add(book , quantity , inplace )


    return redirect('cart:detail_cart')






def remove_from_cart(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    cart = Cart(request)                                 #remove your product from your cart
    cart.remove(book)
    return redirect('cart:detail_cart')





def clear_cart(request):
    cart  = Cart(request)
    cart.clear()                               #This view to remove all products from your cart
    return redirect('cart:detail_cart')




