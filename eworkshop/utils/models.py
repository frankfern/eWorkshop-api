from django.db import models
from django.core.validators import RegexValidator


class TimeModel(models.Model):

    """ Model that can be inherit to obtain fields like 
    create time and modified time"""

    created = models.DateTimeField(
        'created at', auto_now_add=True, help_text='Date time on which object was created')
    modified = models.DateTimeField(
        'modified at ',
        auto_now=True, help_text='Date time on which object was modified')

    class Meta():
        abstract = True
        ordering = ['-created', '-modified']
        get_latest_by = 'created'


class BasicInfoModel(TimeModel):
    """This model can be inherit in order to obtain  basic info """
    phone_regex = RegexValidator(
        regex=r'^\+[1-9]\d{2}\d{3}\d{4}',
        message='Phone number must be enteredin format: +5399999999. Upto 15 digits allowed.'
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(
        max_length=17, blank=True, null=True, validators=[phone_regex])
    cellphone_number = models.CharField(
        max_length=17, blank=False, null=True, validators=[phone_regex])

    class Meta():
        abstract = True


class AdvanceInfoModel(BasicInfoModel):
    """This model is like BasicInfoModel with address and ci fiels """
    ci_regex = RegexValidator(
        regex='\d{11}$', message='Ci must have 11 numbers')

    address = models.CharField(max_length=30, null=False, blank=False)
    ci = models.CharField(
        validators=[ci_regex], unique=True, null=False, blank=False, max_length=11)

    class Meta():
        abstract = True
