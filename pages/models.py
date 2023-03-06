from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactUs(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 20)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.user} : {self.name}'