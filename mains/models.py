
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from users.models import MyUser as usr


class Post(models.Model):
    title = models.TextField(max_length=30)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=15, default = "")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(usr, on_delete=CASCADE)
    domain = models.CharField(max_length=15, default = "")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class PostDomain(models.Model):
    choices = models.CharField(max_length=15)

    def __str__(self):
        return self.choices

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PostType(models.Model):
    choices = models.CharField(max_length=15)

    def __str__(self):
        return self.choices

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)