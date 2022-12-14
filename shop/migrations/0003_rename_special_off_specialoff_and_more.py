# Generated by Django 4.1.3 on 2022-12-09 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_brand_persian_name_category_persian_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Special_Off',
            new_name='SpecialOff',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='no',
            new_name='count',
        ),
        migrations.AddField(
            model_name='product',
            name='off',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='brand',
            name='persian_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='persian_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
