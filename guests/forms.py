from django import forms
from .models import Guest
# from django.contrib.auth.models import User


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
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwags)
    #     self.fields['guest']
