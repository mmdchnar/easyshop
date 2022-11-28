# Generated by Django 4.1.2 on 2022-11-28 05:31

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_laptop_images_alter_mobile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='images',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), blank=True, max_length=255, size=None),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='images',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), blank=True, max_length=255, size=None),
        ),
    ]
