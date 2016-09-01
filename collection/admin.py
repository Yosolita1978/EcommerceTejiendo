from django.contrib import admin
from collection.models import Products
from django.contrib.sites.requests import RequestSite


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Products, ProductsAdmin)
