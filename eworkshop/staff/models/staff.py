from django.db import models
from django.contrib.auth.models import AbstractUser

from eworkshop.utils.models import AdvanceInfoModel


class Staff(AdvanceInfoModel, AbstractUser):

    email = models.EmailField('email address', unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})

    REQUIRED_FIELDS = ['first_name', 'last_name', 'ci']

    def __str__(self):
        return self.first_name

    def change_password(self):
        profile = self.profile
        profile.is_password_changed = True
        profile.save()

    # def create_profile(self):
    #     Profile.objects.create(staff=self)
