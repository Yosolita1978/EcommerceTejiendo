from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('full_name', 'address','city', 'region', 'postal_code', 'country')


admin.site.register(Address, AddressAdmin)