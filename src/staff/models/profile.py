from django.db import models

from utils.models import TimeModel


class Profile(TimeModel):
    """Profile Model.

    A profile holds user statistics and profile picture
    """
    staff = models.OneToOneField('staff.Staff', on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        'profile picture', upload_to='users/pictures')
    is_password_changed = models.BooleanField(default=False)

    def __str__(self):
        return self.staff.first_name
