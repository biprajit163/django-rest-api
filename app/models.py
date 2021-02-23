from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    blogs = ArrayField(models.TextField())

    def __str__(self):
        return self.username

