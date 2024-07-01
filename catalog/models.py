import pathlib
import uuid

from django.db import models


# Рабочая команда для фикстур
# python -Xutf8 manage.py dumpdata catalog --indent=2 --exclude auth.permission --exclude contenttypes -o catalog/fixtures/data.json

def generate_filename_product(instance, filename):
    return generate_filename(instance, filename, 'products')


def generate_filename_blog(instance, filename):
    return generate_filename(instance, filename, 'blog')


def generate_filename(instance, filename, subdir):
    return pathlib.Path(subdir) / f"{uuid.uuid4().hex}.{filename.split('.')[-1]}"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to=generate_filename_product, verbose_name="Превью", blank=True, null=True)
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


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    slug = models.CharField(max_length=200, verbose_name="slug", blank=True, null=True)
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to=generate_filename_blog, verbose_name="Превью", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title}, {self.slug}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['title', 'created_at', 'is_published', 'views_count']