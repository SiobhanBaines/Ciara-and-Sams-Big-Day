import uuid

from django.db import models
from guests.models import Guest


class Checkout(models.Model):
    donation_number = models.CharField(
        max_length=8, null=False, editable=False)
    group_id = models.CharField(max_length=6, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    gift_amount = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_donation_number(self):
        """
        Generate a random, unique donation number using UUID
        """
        return uuid.uuid4().hex[:8].upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the donation number
        if it hasn't been set already
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save()

    def __str__(self):
        return self.donation_number
