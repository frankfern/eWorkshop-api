from django.db import models
from django.db.models.signals import post_save


from eworkshop.utils.models import TimeModel


class ServiceProductManager(models.Manager):
    def create_or_update_quantity(self, service, product, quantity_bought=1):
        object, created = self.get_or_create(
            service=service, product=product
        )
        if not created:
            quantity = object.quantity + quantity_bought

        object.update_quantity(quantity_bought)
        return object


class ServiceProduct(TimeModel):

    service = models.ForeignKey(
        'services.SellService', on_delete=models.CASCADE)
    product = models.ForeignKey(
        'stock.Product', on_delete=models.CASCADE)
    quantity_bought = models.IntegerField(default=1)

    objects = ServiceProductManager()

    def __str__(self):
        return 'Compra: {} Product: {} Cant:{}'.format(
            self.service,
            self.product,
            self.quantity_bought
        )

    def update_quantity(self, quantity=1):
        self.quantity_bought = quantity
        self.save()


def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.service.total_amount


post_save.connect(post_save_update_totals, sender=ServiceProduct)
