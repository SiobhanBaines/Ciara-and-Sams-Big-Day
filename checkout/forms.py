from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = {'gift_amount',}

def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'donation_number' = 'Gift Number',
            'group_id' = 'Family Invitation',
            'date' = 'Date',
            'gift_amount' = 'Amount',
            'full_name': 'Full Name',
        }

        self.fields['gift_amount'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # if field != 'country':
            #     if self.fields[field].required:
            #         placeholder = f'{placeholders[field]} *'
            #     else:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
