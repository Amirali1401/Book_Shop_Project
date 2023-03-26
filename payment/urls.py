from django.urls import path

from . import views as payment_views

app_name = 'payment'

urlpatterns = [
  path('payment_process/' , payment_views.payment_process , name = 'payment_process'),
  ]