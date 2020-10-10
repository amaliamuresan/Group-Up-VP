from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    img = models.ImageField(default='profile.png')

    def __str__(self):
        return f'{self.username} '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
