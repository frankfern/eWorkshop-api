from django.db import models



class Supplier(models.Model):
    
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    ci = models.BigIntegerField()
    address = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    cellphone = models.BigIntegerField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
