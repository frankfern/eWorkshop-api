from django.db import models

from .stock_base_model import StockModel


class SparePart(StockModel):

    type_component = models.ForeignKey(
        'stock.SparePartType', on_delete=models.CASCADE, null=True)
    main_property_header = models.CharField(max_length=25)
