# Generated by Django 3.1.3 on 2020-12-26 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20201130_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sparepart',
            old_name='main_property_value',
            new_name='main_property_header',
        ),
    ]
