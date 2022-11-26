from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50) # name = 'Mobile'
    link = models.CharField(max_length=50) # link = 'mobile/'

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50) # name = 'IPhone 14 Pro Max'
    link = models.CharField(max_length=50) # link = 'iphone-14-pro-max.png'
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category.link = 'mobile/'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50) # name = 'IPhone 14 Pro Max 256GB/6GB'
    link = models.CharField(max_length=50) # link = 'iphone-14-pro-max-256-6/'
    price = models.IntegerField() # price = 52600000
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category.link = 'mobile/'
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # image.link = 'iphone-14-pro-max.png'
    
    def __str__(self):
        return self.name
