# Generated by Django 3.1.3 on 2021-01-21 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which object was modified', verbose_name='modified at ')),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('has_warranty', models.BooleanField(default=False)),
                ('warrantyoff', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('pending', 'pendiente'), ('finished', 'Terminado')], default='pending', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FixSparepart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which object was modified', verbose_name='modified at ')),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SellService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which object was modified', verbose_name='modified at ')),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('has_warranty', models.BooleanField(default=False)),
                ('warrantyoff', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which object was modified', verbose_name='modified at ')),
                ('service_name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which object was modified', verbose_name='modified at ')),
                ('quantity_bought', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.product')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.sellservice')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sellservice',
            name='products',
            field=models.ManyToManyField(through='services.ServiceProduct', to='stock.Product'),
        ),
    ]
