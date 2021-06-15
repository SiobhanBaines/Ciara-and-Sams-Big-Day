from django import forms
from .models import Guest
# from crispy_forms.helper import FormHelper
# from django.contrib.auth.models import User


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = (
            # 'group_id',
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
    #     super(GuestForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(form=self)
    #     self.helper.layout = Layout(
    #         Fieldset('Guest',
    #             Field('group_id', type='hidden')
    #         )
    #     )
