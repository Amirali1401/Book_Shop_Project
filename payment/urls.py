from django.urls import path

from . import views as payment_views

urlpatterns = [
   path('payment_process/' , payment_views.payment_process , name = 'payment_process' ),
   path('payment_callback/' , payment_views.payment_callback , name = 'payment_callback'),
   ]