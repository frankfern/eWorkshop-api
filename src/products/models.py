from django.db import models
from stock.models import Device,Brand,Modelo
from providers.models import Provider



class Product(models.Model):
    CONDITION = (
        ('nuevo', 'Nuevo'),
        ('de_uso', 'De uso')
    )

    STATE = (
        ('disponible','Disponible'),
        ('agotado','Agotado'),
    )

    TYPES = (
        ('sparepart','Pieza de Recambio'),
        ('product','Porducto'),
    )

   
    modelo = models.ForeignKey(
        Modelo, on_delete=models.CASCADE, blank=True)
    

    types = models.CharField(max_length=10,choices=TYPES,null=True)

    sn = models.CharField(max_length=30, null=False)
    price = models.FloatField(null=False)

    state = models.CharField(max_length=30, null=False, choices=STATE,default='disponible')
    condition = models.CharField(max_length=30, null=False, choices=CONDITION)
    quantity = models.IntegerField(null=False)

    description= models.CharField(max_length=100,blank=True)
    supplier = models.ForeignKey(Provider,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.modelo.name
        
