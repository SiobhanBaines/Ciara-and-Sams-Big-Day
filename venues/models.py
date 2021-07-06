from django.db import models


class Venue(models.Model):
    venue_type = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    venue_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.venue_type
