from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "body", "preview", "created_at", "is_published", "views_count",)
