import pathlib
import uuid

from django.db import models


# Рабочая команда для фикстур
# python -Xutf8 manage.py dumpdata catalog --indent=2 --exclude auth.permission --exclude contenttypes -o catalog/fixtures/data.json

def generate_filename(instance, filename):
    return pathlib.Path('products') / f"{uuid.uuid4().hex}.{filename.split('.')[-1]}"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to=generate_filename, verbose_name="Превью", blank=True, null=True)
    category = models.ForeignKey(to="Category", on_delete=models.SET_NULL, verbose_name="Категория", blank=True,
                                 null=True, related_name="products")
    price_per_purchase = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name}, {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name', 'category', 'price_per_purchase']


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Contact(models.Model):
    country = models.CharField(max_length=200, verbose_name="Страна")
    INN = models.CharField(max_length=50, verbose_name="ИНН")
    address = models.CharField(max_length=200, verbose_name="Адрес")

    def __str__(self):
        return f"{self.country}, {self.INN}, {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
