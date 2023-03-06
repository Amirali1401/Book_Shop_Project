from django.urls import path

from . import views as accounts_views

urlpatterns = [
   path('signup/' , accounts_views.register , name = 'register'),

   ]