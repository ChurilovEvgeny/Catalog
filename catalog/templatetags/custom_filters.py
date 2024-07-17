from django import template

from catalog.models import ProductVersion

register = template.Library()


@register.filter()
def make_media_path(data):
    if data:
        return f'/media/{data}'
    return '#'


@register.filter
def get_active_version(obj):
    queryset = obj.get_queryset()
    if not queryset:
        return "Версия не указана"
    return queryset.filter(is_active=True).first().version_name
