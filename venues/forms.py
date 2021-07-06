from django import forms
from .models import Venue


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = (
            'venue_type',
            'name',
            'address_line_1',
            'address_line_2',
            'city',
            'county',
            'postcode',
            'email',
            'phone_number',
            'venue_url',
            'image',
        )
