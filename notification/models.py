from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Notification(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    text = models.TextField()
    url_notification = models.URLField(null = True , blank = True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}  :{self.text}'




class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    category = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.title)




class Answer(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    answer = models.TextField(blank=False, null=False)
    post = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)