from django.db import models
from django.db.models.signals import m2m_changed


from .base_service import BaseService


class SellService(BaseService):

    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        'stock.Product',
        through='services.ServiceProduct',
        through_fields=('service', 'product'),
        serialize=True
    )

    @property
    def total_amount(self,):
        self.price = sum([
            ptb.quantity * ptb.product.price for ptb in self.products_related()
        ])
        self.save()

    def products_related(self):
        return self.buyservice_set.select_related('product')


def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()


m2m_changed.connect(update_totals, sender=SellService.products.through)
