from django.db.models import Model, CharField, SmallIntegerField,\
    BigIntegerField, ForeignKey, FloatField, IntegerField, CASCADE

from django_mysql.models import ListCharField



class Category(Model):
    name = CharField(max_length=50, unique=True)
    link = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Brand(Model):
    name = CharField(max_length=50, unique=True)
    link = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Mobile(Model):
    name = CharField(max_length=50, unique=True)
    link = CharField(max_length=50, unique=True)
    images = ListCharField(CharField(max_length=255), max_length=255)
    price = BigIntegerField()
    count = IntegerField(default=1)
    brand = ForeignKey(Brand, CASCADE)
    category = ForeignKey(Category, CASCADE, default=1)
    size = FloatField()
    display_type = CharField(max_length=50)
    camera_resolution = SmallIntegerField()
    os = CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Laptop(Model):
    name = CharField(max_length=50, unique=True)
    link = CharField(max_length=50, unique=True)
    images = ListCharField(CharField(max_length=255), max_length=255)
    price = BigIntegerField()
    count = IntegerField(default=1)
    size = FloatField()
    brand = ForeignKey(Brand, CASCADE)
    category = ForeignKey(Category, CASCADE, default=2)
    cpu_serie = CharField(max_length=50)
    ram = SmallIntegerField()
    ram_type = CharField(max_length=50)
    graphic_brand = CharField(max_length=50)
    resolution = CharField(max_length=50)
    
    def __str__(self):
        return self.name

