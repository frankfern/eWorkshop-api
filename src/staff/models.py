from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):

    address = models.CharField(max_length=30, null=True, blank=True)
    ci = models.IntegerField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
