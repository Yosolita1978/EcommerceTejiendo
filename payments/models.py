from __future__ import unicode_literals
from django.conf import settings
from django.db import models

COUNTRY_CHOICES =(
    (u'CAN', u'Canada'),
    (u'MEX', u'Mexico'),
    (u'USA', u'United States'),
)

PAYMENT_STATUS_CHOICES =(
    (u'succesful', u'Succesful'),
    (u'fail', u'Fail'),
)

class Address(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='addresses')
    full_name = models.CharField(max_length=255) 
    address = models.TextField()
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255, verbose_name=u'State/Province/Region')
    postal_code = models.CharField(max_length=16, verbose_name=u'Postal Code')
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES)

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    transaction_id = models.CharField(max_length=512)
    product = models.ForeignKey('collection.Products')
    status = models.CharField(max_length=2, choices=PAYMENT_STATUS_CHOICES)



        
