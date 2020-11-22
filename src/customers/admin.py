from django.contrib import admin

from customers.models.contacts import Contact
from .models import Customer, Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Contact)
