from django.shortcuts import render , redirect , get_object_or_404

from .cart import Cart
from .forms import AddToCartFormBook
from books.models import Book
# Create your views here.

def detail_view_cart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_cart'] = AddToCartFormBook(initial={'quantity':item['quantity'] , 'inplace':True})

    return render(request ,'cart/detail_view_cart.html' , context = {'cart':cart})



def add_to_cart(request , book_id):
    cart =  Cart(request)
    book = get_object_or_404(Book , id = book_id)
    form = AddToCartFormBook(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        inplace = cleaned_data['inplace']
        cart.add(book , quantity , inplace )

    return redirect('detail_cart')


def remove_from_cart(request , book_id):
    cart = Cart(request)
    book = get_object_or_404(Book  ,id = book_id)
    cart.remove(book)
    return redirect('detail_cart')
