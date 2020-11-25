from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SellService)
admin.site.register(models.FixService)
admin.site.register(models.ServiceType)
