from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField()
    creation_date = models.DateTimeField(auto_add_now=True)
