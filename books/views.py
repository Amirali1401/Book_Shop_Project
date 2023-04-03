from django.shortcuts import render, redirect , get_object_or_404 , reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.db.models import Q

from .models import Book , Comment , Wishlist
from .forms import CommentForm
from cart.forms import AddToCartFormBook
# Create your views here.

@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index_1.html', context={'books' : books})




class SearchResultsList(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/index_1.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(name__icontains=query)
        )


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



@login_required()
def add_to_wishlist(request,book_id):

   book = get_object_or_404(Book,id=book_id)
   wished_book,created = Wishlist.objects.get_or_create(book=book,
   slug = book.slug,
   user = request.user,
   )

   messages.info(request,'The item was added to your wishlist')
   return redirect('index')




@login_required()
def remove_from_wishlist(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    Wishlist.objects.filter(user = request.user , book = book , slug = book.slug).delete()
    return redirect('index')



