# Generated by Django 5.0.4 on 2025-01-06 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0004_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]