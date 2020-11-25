from django.db import models
from utils.models import TimeModel


class ServiceType(TimeModel):

    service_name = models.CharField(max_length=10, blank=False)

    def __str__(self) -> str:
        return self.service_name
