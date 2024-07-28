# Generated by Django 4.2.14 on 2024-07-28 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0009_alter_productversion_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите владельца товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Products', to=settings.AUTH_USER_MODEL, verbose_name='Владелец товара'),
        ),
    ]
