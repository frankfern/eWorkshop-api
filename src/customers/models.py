from django.db import models


class Customer(models.Model):
    """
    Customer Model
    """
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.BigIntegerField()
    cellphone = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    contact with client
    """
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    time = models.DateTimeField()
