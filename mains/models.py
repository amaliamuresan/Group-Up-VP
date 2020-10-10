
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from users.models import MyUser as usr


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=15, choices=[("paid", "paid"), ("not-paid", "not-paid")], default = "")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(usr, on_delete=CASCADE)
    domain = models.CharField(max_length=15, choices=[("software", "software"), ("hardware", "hardware")], default = "")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
