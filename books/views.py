from django.shortcuts import render, redirect , get_object_or_404 , reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Book , Comment , Wishlist
from .forms import CommentForm
from cart.forms import AddToBooktCartForm
from notification.models import Notification
# Create your views here.



class Index(LoginRequiredMixin , generic.ListView):

    model = Book
    template_name = 'books/index_1.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['books'] = Book.objects.all()
        context['unread_notifications'] = Notification.objects.filter(read = False , user = self.request.user).order_by('id')
        return context

    # def get(self , request):
    #      books = Book.objects.filter(user= self.request.user).order_by('id')
    #      p = Paginator(books , 1)
    #      page_number = request.GET.get('page')
    #      page_obj = p.get_page(page_number)
    #      unread_notification =  Notification.objects.filter(read=False).count()
    #      return render(request , 'books/index_1.html' , context={'books':books , 'unread_notifications':unread_notification , 'page_obj':page_obj})






class SearchResultsList(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/index_1.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(author__icontains = query)
        )


@login_required()
def detail_views_book(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    form = CommentForm()
    add_to_cart = AddToBooktCartForm()
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


