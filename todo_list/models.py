from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class todo_list(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    task = models.TextField()
    date = models.DateTimeField(auto_now=True,auto_now_add=False)


