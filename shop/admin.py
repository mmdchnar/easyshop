from django.contrib import admin
from django.forms import ModelForm
from django.utils.html import format_html
from .models import Mobile, Laptop, Category, Brand, Header,\
     SpecialOff, Product, Image, Detail, Account, Session


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 0


class SessionInline(admin.StackedInline):
    model = Session
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product:', {"fields": [
            'name',
            'email',
            'password',
        ], }),)

    inlines = [SessionInline]

    list_display = ('name', 'email')


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product:', {"fields": [
            'name',
            'count',
            'category',
            'brand',
            'price',
            'off',
        ], }),)

    inlines = [ImageInline, DetailInline]

    list_display = ('name', 'category', 'price', 'Link', 'count')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.name)
    Link.allow_tag = True


class MobileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Mobile:', {"fields": [
            'product',
            'size',
            'display_type',
            'camera_resolution',
            'os',
        ], }),)
    list_display = ('product', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.product.name)
    Link.allow_tag = True


class LaptopAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Laptop:', {"fields": ([
            'product',
            'size',
            'cpu_serie',
            'ram',
            'ram_type',
            'graphic_brand',
            'resolution',
        ]), }),)
    list_display = ('product', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.product.name)
    Link.allow_tag = True


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category:', {"fields": (['name', 'persian_name']), }),
    )
    list_display = ('name', 'persian_name', 'Link')

    def Link(self, obj):
        return format_html('<a href="/{0}">{0}</a>', obj.name)

    Link.allow_tag = True


class BrandAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand:', {"fields": (['name', 'persian_name']), }),
    )
    list_display = ('name', 'persian_name', 'Link')

    def Link(self, obj):
        return format_html('<a href="/{0}">{0}</a>', obj.name)
    Link.allow_tag = True


class HeaderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header:', {
         "fields": (['product', 'sub_title', 'description', 'image']), }),
    )
    list_display = ('product', 'image', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.product.name)
    Link.allow_tag = True


class Special_OffAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Special OFF:', {"fields": ([
            'product',
            'image',
            'time',
            'price',
            'off',
            'detail_1',
            'detail_2',
            'detail_3',
        ]), }),
    )
    list_display = ('product', 'off', 'time', 'Link')

    def Link(self, obj):
        return format_html('<a href="/product/{0}">{0}</a>', obj.product.name)
    Link.allow_tag = True

    def has_add_permission(self, request):
        ret_val = super().has_add_permission(request)
        if ret_val and SpecialOff.objects.exists():
            ret_val = False
        return ret_val


admin.site.register(Account, AccountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SpecialOff, Special_OffAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Mobile, MobileAdmin)
admin.site.register(Laptop, LaptopAdmin)
