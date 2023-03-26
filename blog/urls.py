from django.urls import path

from . import views as blog_views

urlpatterns = [
   path('write_blog/' , blog_views.write_view_blog , name = 'write_blog'),
   ]