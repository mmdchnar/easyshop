from django.db.models import Model, CharField, SmallIntegerField, \
    BigIntegerField, ForeignKey, FloatField, IntegerField, DateTimeField, CASCADE


class Category(Model):
    name = CharField(max_length=50, unique=True)
    persian_name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Brand(Model):
    name = CharField(max_length=50, unique=True)
    persian_name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=50, unique=True)
    price = BigIntegerField()
    off = BigIntegerField(default=0)
    count = IntegerField(default=1)
    brand = ForeignKey(Brand, CASCADE)
    category = ForeignKey(Category, CASCADE)
    views = IntegerField(default=0)

    def __str__(self):
        return self.name


class Mobile(Model):
    product = ForeignKey(Product, CASCADE)
    size = FloatField()
    display_type = CharField(max_length=50)
    camera_resolution = SmallIntegerField()
    os = CharField(max_length=50)

    def __str__(self):
        return self.product.name


class Laptop(Model):
    product = ForeignKey(Product, CASCADE)
    size = FloatField()
    cpu_serie = CharField(max_length=50)
    ram = SmallIntegerField()
    ram_type = CharField(max_length=50)
    graphic_brand = CharField(max_length=50)
    resolution = CharField(max_length=50)

    def __str__(self):
        return self.product.name


class Header(Model):
    product = ForeignKey(Product, CASCADE)
    sub_title = CharField(max_length=50)
    description = CharField(max_length=250)
    image = CharField(max_length=50)

    def __str__(self):
        return self.product.name


class Detail(Model):
    product = ForeignKey(Product, CASCADE)
    name = CharField(max_length=50)
    detail = CharField(max_length=2000)

    def __str__(self):
        return self.name


class SpecialOff(Model):
    product = ForeignKey(Product, CASCADE, default=2)
    image = CharField(max_length=50)
    time = DateTimeField()
    price = BigIntegerField()
    off = SmallIntegerField()
    detail_1 = CharField(max_length=50)
    detail_2 = CharField(max_length=50)
    detail_3 = CharField(max_length=50)

    def __str__(self):
        return self.product.name


class Image(Model):
    product = ForeignKey(Product, CASCADE)
    name = CharField(max_length=50)

    def __str__(self):
        return self.product.name
