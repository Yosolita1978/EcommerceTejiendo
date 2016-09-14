from django.conf.urls import url
from django.views.generic.list import ListView
from .views import products_detail
from collection.models import Products


urlpatterns = [
    url(r'^$',
        ListView.as_view(model=Products, context_object_name='products', template_name='products/products.html'),
        name='catalog'),
    url(r'^(?P<slug>[-\w]+)/$',
        products_detail, name='products_detail'),
]