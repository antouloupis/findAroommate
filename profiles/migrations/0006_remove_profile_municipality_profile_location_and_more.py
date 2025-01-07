# Generated by Django 5.1 on 2024-12-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_email_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='municipality',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(choices=[('18-30', '18-30'), ('31-40', '31-40'), ('41-50', '41-50'), ('51-60', '51-60'), ('60+', '60+'), ('Other', 'Other')], default='Other', max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pets',
            field=models.CharField(choices=[('I like them', 'I like them'), ('I dislike them', 'I dislike them'), ('I like them, and have one (that will stay with me)', 'I like them, and have one (that will stay with me)')], default='I like them', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Any', 'Any')], default='Any', max_length=20),
        ),
    ]
