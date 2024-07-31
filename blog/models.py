from django.db import models

from utils.utils import generate_filename_blog


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    slug = models.CharField(max_length=200, verbose_name="slug", blank=True, null=True)
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to=generate_filename_blog, verbose_name="Превью", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title}, {self.slug}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['title', 'created_at', 'is_published', 'views_count']

        permissions = [
                ('can_control_blog', 'Может управлять блогами'),
            ]

