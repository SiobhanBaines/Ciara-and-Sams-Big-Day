from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    selected = models.BooleanField(default=False)
    supplier_url = models.CharField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
