# Generated by Django 5.0.6 on 2024-07-17 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_productversion_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_versions', to='catalog.product', verbose_name='Продукт'),
        ),
    ]
