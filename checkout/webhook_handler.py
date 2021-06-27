# Taken from CI Stripe Part 10 & 11
from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_even(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment_intent.succeeded webhook event from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle a payment_intent.failed webhook event from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
