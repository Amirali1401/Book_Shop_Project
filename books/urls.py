from django.urls import path

from . import views as books_view

urlpatterns = [
  #books urls
  path('' , books_view.Index.as_view() , name = 'index'),
  path('<int:book_id>/detail_books/' , books_view.detail_views_book , name = 'detail_books'),
  path('<int:book_id>/create_comment/' , books_view.CreateCommentBook.as_view() , name = 'create_comment'),
  path('search/' , books_view.SearchResultsList.as_view() , name ='search_result'),

  #wishlist urls
  path('<int:book_id>/add_to_wishlist/' , books_view.add_to_wishlist , name = 'add_to_wishlist'),
  path('<int:book_id>/remove_from_wishlist/' , books_view.remove_from_wishlist , name = 'remove_from_wishlist'),
  ]