from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = (
            'first_name',
            'last_name',
            'plus_one',
            'address_line_1',
            'address_line_2',
            'city',
            'county',
            'country',
            'postcode',
            'email',
            'phone_number',
        )
