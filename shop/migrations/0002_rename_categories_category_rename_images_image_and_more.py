# Generated by Django 4.1.2 on 2022-11-26 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]