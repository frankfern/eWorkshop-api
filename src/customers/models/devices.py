from django.db import models

from stock.models import BaseStock


class CustomerDevice(BaseStock):

    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE, null=False)
