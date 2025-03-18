from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120) # required max_length
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField()
    featured = models.BooleanField(default=True)