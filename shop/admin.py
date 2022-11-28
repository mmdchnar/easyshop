from django.contrib import admin
from django.forms import ModelForm
from django.utils.html import format_html
from .models import Mobile, Laptop, Category, Brand



class MobileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Mobile', {"fields": [
            'name',
            'link',
            'category',
            'brand',
            'price',
            'size',
            'display_type',
            'camera_resolution',
            'os',
            ],}),
        ('Images', {"fields": ['images']}),
    )
    list_display = ('name', 'brand', 'price', 'custom_link_field')

    def custom_link_field(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    custom_link_field.allow_tag = True


class LaptopAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Laptop', {"fields": ([
            'name',
            'link',
            'category',
            'brand',
            'price',
            'size',
            'cpu_serie',
            'ram',
            'ram_type',
            'graphic_brand',
            'resolution',
            ]),}),
        ('Images', {"fields": ['images']},),
    )
    list_display = ('name', 'brand', 'price', 'link_field')

    def link_field(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    link_field.allow_tag = True


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category', {"fields": (['name', 'link']),}),
    )
    list_display = ('name', 'link')


class BrandAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Laptop', {"fields": (['name', 'link']),}),
    )
    list_display = ('name', 'link')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Mobile, MobileAdmin)
admin.site.register(Laptop, LaptopAdmin)
