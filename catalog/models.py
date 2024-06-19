from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to="products/", verbose_name="Превью", blank=True, null=True)
    category = models.ForeignKey(to="Category", on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True, related_name="products")
    price_per_purchase = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания")
    update_at = models.DateField(verbose_name="Дата последнего изменения")
    manufactured_at = models.DateField(verbose_name="Дата производства продукта", default=None)

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
