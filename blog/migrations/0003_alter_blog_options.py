# Generated by Django 4.2.14 on 2024-07-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_views_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['title', 'created_at', 'is_published', 'views_count'], 'permissions': [('can_control_blog', 'Может управлять блогами')], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
    ]
