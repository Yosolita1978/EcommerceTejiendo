from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    main_picture = models.ForeignKey('ProductPicture', blank=True, null=True)
    overview = models.TextField()

    def __str__(self):
        return self.name

class ProductPicture(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey('Products', related_name='pictures')

    def __str__(self):
        return '%s (%s)' %(self.product, self.image)


