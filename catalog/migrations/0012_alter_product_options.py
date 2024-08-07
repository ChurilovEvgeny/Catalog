# Generated by Django 4.2.14 on 2024-07-31 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'category', 'price_per_purchase'], 'permissions': [('change_is_published', 'Can change product publish status'), ('change_description', 'Can change product description'), ('change_category', 'Can change product category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
