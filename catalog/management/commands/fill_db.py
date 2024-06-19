import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def load_json() -> tuple[list, list]:
        with open("catalog/fixtures/data.json", "r", encoding="utf-8") as f:
            dict_json = json.load(f)
            d_category = []
            d_product = []
            for d in dict_json:
                if d['model'] == "catalog.product":
                    d_product.append({'pk': d['pk']} | d['fields'])
                else:
                    d_category.append({'pk': d['pk']} | d['fields'])

            return d_category, d_product

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        d_category, d_product = Command.load_json()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in d_category:
            category_for_create.append(
                Category(**category)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in d_product:
            product["category"] = Category.objects.get(pk=product["category"])
            product_for_create.append(
                Product(**product)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
