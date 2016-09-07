from django.contrib import admin
from collection.models import Products, ProductPicture
from django.contrib.sites.requests import RequestSite

class ProductPictureInline(admin.TabularInline):
    model = ProductPicture


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductPictureInline,]

class ProductPictureAdmin(admin.ModelAdmin):
    model = ProductPicture
    list_display = ('product', 'image',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductPicture, ProductPictureAdmin)
