from django.db import models

from utils.models import AdvanceInfoModel


class Supplier(AdvanceInfoModel):

    def __str__(self):
        return self.first_name
