# Generated by Django 3.1.3 on 2021-01-24 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_auto_20210124_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='cellphone_number',
            field=models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be enteredin format: +5399999999. Upto 15 digits allowed.', regex='^\\+[1-9]\\d{2}\\d{3}\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='ci',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Ci must have 11 numbers', regex='\\d{11}$')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be enteredin format: +5399999999. Upto 15 digits allowed.', regex='^\\+[1-9]\\d{2}\\d{3}\\d{4}')]),
        ),
    ]
