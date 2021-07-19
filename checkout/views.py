from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from .models import Checkout
from guests.models import Guest
from .forms import CheckoutForm
from decimal import Decimal
from django.contrib.auth.decorators import login_required

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ cache data for Stripe intent """
    # Taken from CI Stripe Part 14 and modified to use site data
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'gift_amount': json.dumps(request.session.get('gift_amount', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, you payment cannot be \
            processed at the moment. Please try later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """ Process a gift donation payment """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        gift_amount = request.session.get('gift_amount', {})
        # save fields to be used outside checkout.html template
        group_id = request.POST['group_id']
        email = request.POST['email']
        first_name = request.POST['first_name']

        # Get the billing details from the template
        guest_data = {
            'group_id': request.POST['group_id'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'email': request.POST['email'],
        }

        # instantiate form data
        form = CheckoutForm(guest_data)

        if form.is_valid():
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe_pid = pid
            # Create new checkout object
            checkout = Checkout(
                group_id=group_id,
                gift_amount=gift_amount,
                stripe_pid=stripe_pid,
                )
            checkout.save()

            # pick up records from Guest model
            guests = Guest.objects.filter(group_id=request.user)

            # check if payment is by a guest, update guest's email,
            #   add gift details
            for guest in guests:

                # is payment by a guest
                if (form['first_name'] == guest.first_name) and (
                        form['last_name'] == guest.last_name):
                    # Update Guest email
                    guest.email = form['email']
                # update all guests in group
                guest.gift_chosen = True
                guest.gift_name = 'Money'
                guest.gift_value += Decimal(gift_amount)
                guest.save()

            # Stripe setup
            amount = float(gift_amount)         # convert string to decimal
            stripe_total = round(amount * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            # get most recent donation number
            donation_number = Checkout.objects.filter(group_id=group_id).last()

            checkout_email(donation_number, email, first_name)

            return redirect(reverse(
                'checkout_success',
                args=[donation_number, email]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        gift_amount = request.session.get('gift_amount', {})
        if not gift_amount:
            gift_amount = 0

        # Load template with lead guest details
        guests = Guest.objects.filter(group_id=request.user)
        guest = ''
        for g in guests:
            if guest == '':
                guest = g

        form = CheckoutForm(instance=guest)       # contains guest details
        amount = float(gift_amount)               # convert string to decimal
        stripe_total = round(amount * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing from your environment.')

    group_id = guest
    template = 'checkout/checkout.html'
    context = {
        'group_id': group_id,
        'guest': guest,
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


@login_required
def checkout_success(request, donation_number, email):
    """
    Handle successful checkouts
    """
    # Taken from CI Stripe and modified to fit site requirements
    messages.success(request, f'Gift successfully processed! \
        Your gift donation number is {donation_number}. A confirmation \
        email will be sent to {email}.')

    # form = CheckoutForm
    checkout = get_object_or_404(Checkout, donation_number=donation_number)
    template = 'checkout/checkout_success.html'
    context = {
        'email': email,
        'checkout': checkout,

    }

    return render(request, template, context)


def checkout_email(donation_number, email, first_name):
    """ Send checkout email """

    checkout = get_object_or_404(Checkout, donation_number=donation_number)

    context = {
        'first_name': first_name,
        'checkout': checkout,
    }

    # The below process for loading the email was taken from
    #   MasterCodeOnline and modifiied for the specific emails
    subject = 'Confirmation of gift Payment Reciept'
    with open('checkout/templates/checkout/email.txt') as f:
        checkout_message = f.read()
    message = EmailMultiAlternatives(
        subject=subject, body=checkout_message,
        from_email=settings.DEFAULT_FROM_EMAIL, to=[email, ])
    template = get_template('checkout/email.html').render(context)
    message.attach_alternative(template, 'text/html')
    message.send()
