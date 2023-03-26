from django.shortcuts import render , get_object_or_404

from order.models import Order

# Create your views here

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order , id = order_id)
    tooman_total_price = order.get_total_porice()


