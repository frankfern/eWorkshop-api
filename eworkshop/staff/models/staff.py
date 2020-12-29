from django.db import models
from django.contrib.auth.models import AbstractUser

from eworkshop.utils.models import AdvanceInfoModel


class Staff(AdvanceInfoModel, AbstractUser):

    email = models.EmailField('email address', unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})

    REQUIRED_FIELDS = ['first_name', 'last_name', 'ci']


def __str__(self):
    return self.first_name
