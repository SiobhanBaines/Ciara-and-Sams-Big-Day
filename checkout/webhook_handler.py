# Followed the CI stripe videos to create this file
#       and modified to work with this site
from django.http import HttpResponse
from .models import Checkout
from guests.models import Guest
from decimal import Decimal

import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic, unknown or unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        gift_amount = round(intent.amount / 100, 2)

        group_id = intent.metadata.username

        checkout_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                checkout = Checkout.objects.get(
                    group_id__iexact=group_id,
                    gift_amount=gift_amount,
                    stripe_pid=pid,
                )
                checkout_exists = True
                break

            except Checkout.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if checkout_exists:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS : \
                     Verified gift donation already indatabase', status=200)
        else:
            try:
                # checkout = Checkout.objects.create()
                checkout = Checkout(
                    group_id=group_id, gift_amount=gift_amount, stripe_pid=pid)

                checkout.save()
                # pick up records from Guest model
                guests = Guest.objects.filter(group_id=group_id)
                # check if payment is by a guest, update
                #       guest's email, add gift details
                for guest in guests:

                    # update all guests in group
                    guest.gift_chosen = True
                    guest.gift_name = 'Money'
                    guest.gift_value += Decimal(gift_amount)
                    guest.save()
            except Exception as e:
                if checkout:
                    checkout.deleted()
                    if guest.gift_value == Decimal(gift_amount):
                        guest.gift_chosen = ''
                    guest.gift_value -= Decimal(gift_amount)
                    guest.save()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: \
                        {e}', status=500)
        return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | SUCCESS: \
                        Created gift donation in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Payment failed webhook received: {event["type"]}',
            status=200)
