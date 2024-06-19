from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price_per_purchase", "category")


@admin.register(Category)
class CateoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
