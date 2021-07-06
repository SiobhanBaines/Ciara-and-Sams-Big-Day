from django.contrib import admin
from .models import Venue


class VenueAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'address_line_1',
        'address_line_2',
        'city',
        'county',
        'country',
        'postcode',
        'email',
        'phone_number',
        'venue_url',
        'image',
    )
    ordering = ('type', 'name')


admin.site.register(Venue)
