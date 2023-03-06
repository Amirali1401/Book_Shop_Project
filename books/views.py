from django.shortcuts import render, redirect , get_object_or_404 , reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Book , Comment
from .forms import CommentForm
from cart.forms import AddToCartFormBook
# Create your views here.

@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index_1.html', context={'books' : books})





@login_required()
def detail_views_book(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    form = CommentForm()
    add_to_cart = AddToCartFormBook()
    return render(request , 'books/detail_views_book.html' , context={'book':book , 'form':form , 'add_to_cart':add_to_cart})




# @login_required()
# def create_comment_book(request , book_id):
#     book = get_object_or_404(Book , id = book_id)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         obj_form = form.save(commit=False)
#         obj_form.user = request.user
#         obj_form.book = book
#         obj_form.save()
#
#     return redirect('index')


class CreateCommentBook(LoginRequiredMixin , generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        book_id = int(self.kwargs['book_id'])
        book = get_object_or_404(Book , id = book_id)
        obj_form.book = book
        obj_form.save()
        return super().form_valid(form)
