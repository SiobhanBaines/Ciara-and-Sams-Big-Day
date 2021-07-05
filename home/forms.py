# Code originally created by Jaysha of Ordinary Coders.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from guests.models import Guest


class NewUserForm(UserCreationForm):
    # New User Form to enable registered individual to be staff
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class RSVPForm(forms.Form):
    # RSVP form to allow guests to accept or decline the invitation

    class Meta:
        model = Guest
        fields = (
            'Guest object',
            "id",
            "group_id",
            "first_name",
            "last_name",
            "accepted",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
