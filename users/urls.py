from django.conf.urls import url
from .views import user_profile 


urlpatterns = [
    url(r'^profile/$',
        user_profile, name='user_profile'),
]