from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChangePassword(models.Model):
    current_password = models.CharField(max_length=20)
    new_password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.current_password} : {self.new_password}'