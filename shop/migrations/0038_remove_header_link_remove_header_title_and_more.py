# Generated by Django 4.1.2 on 2022-11-30 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_alter_laptop_laptop_alter_mobile_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='link',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title',
        ),
        migrations.RemoveField(
            model_name='special_off',
            name='link',
        ),
        migrations.RemoveField(
            model_name='special_off',
            name='title',
        ),
        migrations.AddField(
            model_name='header',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AddField(
            model_name='special_off',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='laptop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]