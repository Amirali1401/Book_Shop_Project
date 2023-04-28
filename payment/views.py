import json

from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse

from order.models import Order

import requests

# Create your views here.


def payment_process(request):
    order_id  = request.session.get('order_id')
    order = get_object_or_404(Order , id = order_id)
    tooman_price = order.get_total_price()

    zarinpal_request_url = "https://api.zarinpal.com/pg/v4/payment/request.json"

    request_header = {
         'accept':'application/json',
          'content-type':'application/json'
    }

    request_data = {
        'merchant_id':settings.ZARINPAL_MARCHENT_ID,
        'amount':tooman_price,
        'description':f'{order.id} : {order.first_name} : {order.last_name}',
        'callback_url':'https://127.0.0.1:8000',
    }

    res = requests.post(url = zarinpal_request_url , data = json.dumps(request_data) ,  headers = request_header)
    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority = authority))

    else:
       return HttpResponse('Error from zarinpal')




def payment_callback(request):
    payment_status = request.GET.get('Status')
    payment_authority = request.GET.get('Authority')
    order = get_object_or_404(Order , zarinpal_authority = payment_authority )
    tooman = order.get_total_price()
    if payment_status  == 'OK':
        request_header = {
            'accept':'application/json',
            'content-type':'application/json',
        }

        request_data = {
            'merchant_id':settings.ZARINPAL_MARCHENT_ID,
            'amount':tooman,
            'authority':payment_authority,
        }

        res = requests.post(url = "https://api.zarinpal.com/pg/v4/payment/verify.json" , data = json.dumps(request_data) , headers = request_header)

        if 'data' in res.json() and ('errors' in res.json()['data'] or len(res.json()['data'])):
            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()

                return HttpResponse('پرداخت شما با موفقست انجام شد.')

            elif payment_code ==101:
                return HttpResponse('پرداخت شما با موفقست انجام شد . البته این تراکنش قبلا هم انجام شده')


            else:
                errors_massage = data['errors']['message']
                errors_code = data['errors']['code']
                return  HttpResponse(f'تراکنش ناموفق هست {errors_code} " {errors_massage}')

