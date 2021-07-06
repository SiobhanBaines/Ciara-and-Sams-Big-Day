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
            'lat',
            'lng',
            'image',
        )

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'venue_type': 'Ceremony/Recpetion',
                'name': 'Venue Name',
                'address_line_1': 'Address Line',
                'address_line_2': 'Address Line',
                'city': 'City',
                'county': 'County',
                'postcode': 'Post Code',
                'email': 'Contact Email Address',
                'phone_number': 'Telephone Number',
                'venue_url': 'Venue Wedsite',
                'lat': 'Location Latitude',
                'lng': 'Location Longditude',
            }

            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
