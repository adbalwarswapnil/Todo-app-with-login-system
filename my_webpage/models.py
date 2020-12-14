from django.db import models

# Create your models here.

class Comment_section(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pin_code = models.IntegerField()
    date = models.DateTimeField()