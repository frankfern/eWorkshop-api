from django.db.models.signals import post_save

from eworkshop.services.models import ServiceProduct


def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.service.total_amount


post_save.connect(post_save_update_totals, sender=ServiceProduct)
