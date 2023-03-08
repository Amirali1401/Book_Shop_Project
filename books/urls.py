from django.urls import path

from . import views as books_view

urlpatterns = [
  path('' , books_view.index , name = 'index'),
  path('<int:book_id>/detail_books/' , books_view.detail_views_book , name = 'detail_books'),
  path('<int:book_id>/create_comment/' , books_view.CreateCommentBook.as_view() , name = 'create_comment'),

  #wishlist urls
  path('<int:book_id>/add_to_wishlist/' , books_view.add_to_wishlist , name = 'add_to_wishlist'),
  path('<int:book_id>/remove_from_wishlist/' , books_view.remove_from_wishlist , name = 'remove_from_wishlist'),
  ]