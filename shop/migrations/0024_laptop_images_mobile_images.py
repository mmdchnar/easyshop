# Generated by Django 4.1.2 on 2022-11-28 05:35

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_remove_laptop_images_remove_mobile_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='images',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), blank=True, max_length=255, size=None),
        ),
        migrations.AddField(
            model_name='mobile',
            name='images',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), blank=True, max_length=255, size=None),
        ),
    ]