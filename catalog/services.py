from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_cached_category_list():
    if not settings.CACHE_ENABLED:
        return Category.objects.all()

    key = 'category_list'
    category_list = cache.get(key)
    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list)

    return category_list
