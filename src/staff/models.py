from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import AdvanceInfoModel


class Staff(AdvanceInfoModel, AbstractUser):

    email = models.EmailField('email address', unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


def __str__(self):
    return self.first_name
