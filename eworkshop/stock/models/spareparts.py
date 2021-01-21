from django.db import models

from .stock_base_model import StockModel
from eworkshop.services.models.fix_sparepart import FixSparepart


class SparePart(StockModel):

    type_component = models.ForeignKey(
        'stock.SparePartType', on_delete=models.CASCADE, null=True)
    main_property_header = models.CharField(max_length=25)

    @property
    def used_quantity(self):
        quantity = FixSparepart.objects.filter(
            sparepart=self.id).aggregate(models.Sum('quantity'))
        return quantity['quantity__sum']
