# Generated by Django 3.1.3 on 2021-01-21 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellservice',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fixsparepart',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.fixservice'),
        ),
        migrations.AddField(
            model_name='fixsparepart',
            name='sparepart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.sparepart'),
        ),
        migrations.AddField(
            model_name='fixservice',
            name='clients_device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customerdevice'),
        ),
        migrations.AddField(
            model_name='fixservice',
            name='resources',
            field=models.ManyToManyField(through='services.FixSparepart', to='stock.SparePart'),
        ),
        migrations.AddField(
            model_name='fixservice',
            name='service_type',
            field=models.ManyToManyField(to='services.ServiceType'),
        ),
        migrations.AddField(
            model_name='fixservice',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
