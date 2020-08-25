from django.db import models

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
