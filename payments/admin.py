from django.contrib import admin
from .models import Address, Payment


class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('full_name', 'address','city', 'region', 'postal_code', 'country')

class PaymentsAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('user', 'date', 'transaction_id', 'product', 'status')        


admin.site.register(Address, AddressAdmin)
admin.site.register(Payment, PaymentsAdmin)