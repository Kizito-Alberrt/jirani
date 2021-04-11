from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 

    def __str__(self):
        return self.location


class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    hood = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name


class business(models.Model):
    business = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_email = models.CharField(max_length=200)

