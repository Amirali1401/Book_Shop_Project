from django.urls import path

from . import views as accounts_views

urlpatterns = [
   path('signup/' , accounts_views.register , name = 'register'),
   path('change_account/', accounts_views.change_account_view , name ='change_account'),
   path('change_password/' , accounts_views.change_password ),
   ]