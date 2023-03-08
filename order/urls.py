from django.urls import path

from . import views as order_views

urlpatterns = [
    path('order_create/' , order_views.order_create , name ='order_create'),
    ]