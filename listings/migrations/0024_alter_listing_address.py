# Generated by Django 5.1 on 2024-12-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_remove_location_latitude_remove_location_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(default='Unkown address', max_length=255),
        ),
    ]
