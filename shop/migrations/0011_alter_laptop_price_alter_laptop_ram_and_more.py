# Generated by Django 4.1.2 on 2022-11-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_product_category_delete_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='camera_resolution',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]