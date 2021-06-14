from django import forms
from .models import Guest
# from django.contrib.auth.models import User


class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwags)
    #     self.fields['guest']
