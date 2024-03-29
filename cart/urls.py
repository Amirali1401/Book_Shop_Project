from django.urls import path

from . import views as cart_views

app_name = 'cart'

urlpatterns = [
    path('' , cart_views.detail_cart_view , name = 'detail_cart'),
    path('<int:book_id>/add_to_cart/' , cart_views.add_to_cart , name = 'add_to_cart'),
    path('<int:book_id>/remove_from_cart/' , cart_views.remove_from_cart , name = 'remove_from_cart'),
    path('clear/' , cart_views.clear_cart , name = 'clear_cart'),
    ]