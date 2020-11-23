from django.db import models

from stock.models import BaseStock


class CustomerDevice(BaseStock):

    client = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE, null=False)
