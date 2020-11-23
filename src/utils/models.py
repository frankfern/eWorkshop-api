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
        regex=r'\+?2?\d{8-15}$',
        message='Phone number must be enteredin format: +5399999999. Upto 15 digits allowed.'
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)
    cellphone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)

    class Meta():
        abstract = True


class AdvanceInfoModel(BasicInfoModel):
    """This model is like BasicInfoModel with address and ci fiels """
    ci_regex = RegexValidator(
        regex='\d{1,11}$', message='Ci must have 11 numbers')

    address = models.CharField(max_length=30, null=False, blank=False)
    ci = models.PositiveIntegerField(
        validators=[ci_regex], unique=True, null=False, blank=False)

    class Meta():
        abstract = True


class StockModel(TimeModel):

    CONDITION = (
        ('new', 'Nuevo'),
        ('used', 'De uso')
    )
    description = models.CharField(max_length=100, blank=True)
    sn = models.CharField(max_length=30, null=False, blank=True)
    price = models.FloatField(null=False)
    condition = models.CharField(max_length=30, null=False, choices=CONDITION)
    quantity = models.PositiveIntegerField(null=False)
    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.PROTECT, null=True)

    class Meta():
        abstract = True
