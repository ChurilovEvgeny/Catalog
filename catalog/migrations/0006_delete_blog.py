# Generated by Django 5.0.6 on 2024-07-02 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_blog_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
