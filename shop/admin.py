from django.contrib import admin
from django.forms import ModelForm
from django.utils.html import format_html
from .models import Mobile, Laptop, Category, Brand, Header, Special_Off



class MobileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Mobile:', {"fields": [
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
    list_display = ('name', 'brand', 'price', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True


class LaptopAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Laptop:', {"fields": ([
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
    list_display = ('name', 'brand', 'price', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category:', {"fields": (['name', 'link']),}),
    )
    list_display = ('name', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True


class BrandAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand:', {"fields": (['name', 'link']),}),
    )
    list_display = ('name', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True


class HeaderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header:', {"fields": (['title', 'link', 'sub_title', 'description', 'image']),}),
    )
    list_display = ('title', 'image', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True


class Special_OffAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Special OFF:', {"fields": ([
            'title',
            'link',
            'image',
            'time',
            'price',
            'off',
            'detail_1',
            'detail_2',
            'detail_3',
            ]),}),
    )
    list_display = ('title', 'off', 'time', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.link)
    
    Link.allow_tag = True

    def has_add_permission(self, request):
        retVal = super().has_add_permission(request)
        if retVal and Special_Off.objects.exists():
            retVal = False
        return retVal



admin.site.register(Special_Off, Special_OffAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Mobile, MobileAdmin)
admin.site.register(Laptop, LaptopAdmin)
