from django.urls import path

from . import views as books_view

urlpatterns = [
  path('' , books_view.index , name = 'index'),
  path('<int:book_id>/detail_books/' , books_view.detail_views_book , name = 'detail_books'),
  path('<int:book_id>/create_comment/' , books_view.CreateCommentBook.as_view() , name = 'create_comment'),
  ]