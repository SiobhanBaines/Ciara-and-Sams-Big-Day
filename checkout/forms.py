from django import forms
from .models import Guest


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = (
            'first_name',
            'last_name',
            'email',
            'address_line_1',
            'address_line_2',
            'city',
            'county',
            'postcode',
            'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'group_id': 'Guest Group',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'county': 'County',
            'postcode': 'Post Code',
            'country': 'Country',
            'email': 'Email'
        }

        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
