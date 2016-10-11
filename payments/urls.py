from django.conf.urls import url
from .views import address_capture, checkout


urlpatterns = [
    url(r'^address/$',
        address_capture, name='address_form'),
    url(r'^checkout/$',
        checkout, name='checkout'),
]