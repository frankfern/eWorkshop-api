from django.contrib import admin

from eworkshop.customers.models.contacts import Contact
from .models import Customer, Contact, CustomerDevice

# Register your models here.
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(CustomerDevice)
