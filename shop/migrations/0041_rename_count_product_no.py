# Generated by Django 4.1.3 on 2022-12-01 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_rename_laptop_laptop_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='no',
        ),
    ]
