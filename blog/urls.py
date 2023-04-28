from django.urls import path

from . import views as blog_views

urlpatterns = [
   path('' , blog_views.read_view_blog , name = 'list_blogs'),
   path('<int:blog_id>/detail_blog/' , blog_views.detail_view_blog , name = 'detail_blog'),
   path('write_blog/' , blog_views.write_view_blog , name = 'write_blog'),
   path('<int:blog_id>/delete_blog/' , blog_views.delete_view_blog , name = 'delete_blog'),
   ]