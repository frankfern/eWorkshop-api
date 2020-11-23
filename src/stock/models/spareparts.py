from django.db import models

from utils.models import StockModel


class SparePart(StockModel):

    sparepart_device = models.ForeignKey(
        'stock.DeviceModel', on_delete=models.CASCADE, null=True)
    type_component = models.ForeignKey(
        'stock.SparePartType', on_delete=models.CASCADE, null=True)
    main_property_value = models.CharField(max_length=25)
