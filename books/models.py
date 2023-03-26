from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Book(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    numbers = models.PositiveIntegerField(default=0)
    page_numbers = models.PositiveIntegerField(default=0 , null = True , blank = True)
    pages_quality = models.CharField(max_length=20 , null = True , blank=True)
    covers = models.ImageField(upload_to='covers/')
    slug = models.CharField(max_length=30 , null=True , blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def  tell_name(self):
        return f'please tell {self.name}'

    class Meta:
        verbose_name = 'گتاب'
        verbose_name_plural = 'کنابها'


    def __str__(self):
        return f'{self.user} : {self.name}'





class Wishlist(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE)
    slug = models.CharField(max_length=30 , null=True , blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book.name}'



class Comment(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    book = models.ForeignKey(Book , on_delete = models.CASCADE , related_name = 'comments')
    email = models.EmailField()
    text = models.TextField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user} : {self.book}'
