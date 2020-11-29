from django.db import models

from utils.models import TimeModel
from .customers import Customer


class Contact(TimeModel):
    """
    contact with client
    """
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.time
