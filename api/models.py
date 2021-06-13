
from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default="password")
    created = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['id']
