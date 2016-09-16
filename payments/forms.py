from django.forms import ModelForm
from .models import Address

class AddressForm(ModelForm):
    class Meta:
        model = Address
        #exclude = ['user']
        fields = ['full_name', 'address', 'city', 'region', 'postal_code', 'country']

            
        