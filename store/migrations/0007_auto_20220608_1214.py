# Generated by Django 3.0.8 on 2022-06-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220607_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gst',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='productcode',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
