from django.db import models

# Create your models here.
class userss(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    inputPassword = models.CharField(max_length=50)
    status = models.BooleanField()