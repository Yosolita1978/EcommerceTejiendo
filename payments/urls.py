from django.conf.urls import url
from .views import address_capture


urlpatterns = [
    url(r'^address/$',
        address_capture, name='address_form'),
]