from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
        
