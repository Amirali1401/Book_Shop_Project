from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    score = models.PositiveIntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}  : {self.title}'