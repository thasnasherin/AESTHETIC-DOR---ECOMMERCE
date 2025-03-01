# Generated by Django 5.0.4 on 2024-11-20 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('country', models.TextField()),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.cart')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.register')),
            ],
        ),
    ]
