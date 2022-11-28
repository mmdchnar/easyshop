# Generated by Django 4.1.2 on 2022-11-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('size', models.FloatField(default=0)),
                ('cpu_serie', models.CharField(default='', max_length=50)),
                ('ram', models.IntegerField(default=0)),
                ('ram_type', models.CharField(default='', max_length=50)),
                ('graphic_brand', models.CharField(default='', max_length=50)),
                ('resolution', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('size', models.FloatField(default=0)),
                ('display_type', models.CharField(default='', max_length=50)),
                ('camera_resolution', models.IntegerField(default=0)),
                ('os', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=50),
        ),
    ]
