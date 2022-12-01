# Generated by Django 4.1.2 on 2022-11-30 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_alter_laptop_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='laptop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
