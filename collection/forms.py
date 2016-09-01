from django.forms import ModelForm
from collection.models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description',)