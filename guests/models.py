from django.db import models
from django_countries.fields import CountryField


class Guest(models.Model):
    group_id = models.CharField(max_length=6, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    plus_one = models.BooleanField(default=False)
    address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    accepted = models.CharField(max_length=10, null=True, blank=True)
    meal_chosen = models.BooleanField(default=False)
    starter = models.CharField(max_length=80, null=True, blank=True)
    main = models.CharField(max_length=80, null=True, blank=True)
    dessert = models.CharField(max_length=80, null=True, blank=True)
    gift_chosen = models.BooleanField(default=False)
    gift_name = models.CharField(max_length=254, null=True, blank=True)
    gift_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0)


def __str__(self):
    return self.first_name+" "+self.last_name
