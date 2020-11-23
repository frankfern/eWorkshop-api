from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import AdvanceInfoModel


class Staff(AdvanceInfoModel, AbstractUser):

    email = models.EmailField('email address', unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})

    is_staff = models.BooleanField(
        'staff status',
        default=True,
        help_text=(
            'Designates whether the user can log into this admin site.'))

    REQUIRED_FIELDS = ['first_name', 'last_name', 'ci']


def __str__(self):
    return self.first_name
