from django import forms
from .models import Checkout, Guest


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = {'gift_amount', }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'donation_number': 'Gift Number',
            'group_id': 'Family Invitation',
            'date': 'Date',
            'gift_amount': 'Amount',
        }

        self.fields['gift_amount'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = (
            'first_name',
            'last_name',
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
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address_line_1': 'Address Line',
            'address_line_2': 'Address Line',
            'city': 'City',
            'county': 'County',
            'postcode': 'Post Code',
            'country': 'Country',
        }

        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
