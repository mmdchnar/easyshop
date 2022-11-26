from django.contrib import admin
from .models import Category, Product, Image


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category', {"fields": (['name', 'link']),}),
    )
    list_display = ('name', 'link')


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product', {"fields": (['name', 'link', 'price', 'category', 'image']),}),
    )
    list_display = ('name', 'price', 'link', 'category', 'image')


class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Image', {"fields": (['name', 'link', 'category']),}),
    )
    list_display = ('name', 'link', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
