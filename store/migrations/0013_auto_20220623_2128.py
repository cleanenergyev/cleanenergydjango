# Generated by Django 3.0.8 on 2022-06-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220623_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclestock',
            name='available',
            field=models.CharField(default='True', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiclestock',
            name='productdesc',
            field=models.CharField(max_length=120),
        ),
    ]
