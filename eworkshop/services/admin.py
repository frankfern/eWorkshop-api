from django.contrib import admin
from . import models

admin.site.register(models.SellService)
admin.site.register(models.FixService)
admin.site.register(models.ServiceType)
admin.site.register(models.BuyService)
