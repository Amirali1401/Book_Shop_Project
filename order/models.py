from django.db import models
from django.contrib.auth.models import User

from books.models import Book
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} : {self.phone_number}  {self.date_created}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.order_items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete = models.CASCADE , related_name='order_items')
    book =  models.ForeignKey(Book , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order.id} : {self.book.name} : {self.date_created}'



