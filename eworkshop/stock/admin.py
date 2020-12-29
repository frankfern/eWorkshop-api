from django.contrib import admin
from . import models


admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.DeviceType)
admin.site.register(models.DeviceModel)
admin.site.register(models.SparePart)
admin.site.register(models.SparePartType)
