from django.contrib import admin

from catalog.models import Product, Category, Contact, ProductVersion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price_per_purchase", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("pk", "country", "INN", "address")


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ("pk", "product", "version", "version_name", "is_active")
    list_filter = ("product", "is_active")