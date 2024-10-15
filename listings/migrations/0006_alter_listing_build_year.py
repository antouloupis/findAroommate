# Generated by Django 5.1 on 2024-10-11 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_build_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='build_year',
            field=models.SmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2025), django.core.validators.MinValueValidator(1940)]),
        ),
    ]
