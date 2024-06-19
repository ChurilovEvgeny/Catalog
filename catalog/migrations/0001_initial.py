# Generated by Django 5.0.6 on 2024-06-19 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Превью')),
                ('price_per_purchase', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за покупку')),
                ('created_at', models.DateField(verbose_name='Дата создания')),
                ('update_at', models.DateField(verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'category', 'price_per_purchase'],
            },
        ),
    ]
