from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .models import Checkout
from guests.models import Guest
# from .forms import CheckoutForm, GuestForm
from .forms import CheckoutForm

import stripe


@require_POST
def cache_checkout_data(request):
    # request.session['']
    # Taken from CI Stripe Part 14 and modified for site data
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'amount': request.POST.get('gift_amount'),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # print('line 28', gift_amount, amount, save_info, username)
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        messages.error(request, 'Sorry, you payment cannot be \
            processed at the moment. Please try later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        # Get the billing details from the template
        guest_data = {
            # 'group_id': request.POST['group_id'],
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

        form = CheckoutForm(guest_data)
        gift_amount = request.session['gift_amount']

        if form.is_valid():
            objs = []
            # Create Checkout model
            objs.append(
                Checkout(
                    gift_amount=gift_amount
                    # group_id=form['group_id']
                )
            )
            # checkout.save()

            # pick up records from Guest model
            guests = Guest.objects.filter(group_id=request.user)
            # check if form first & last name match any guest record
            for g_num in guests:
                print("line 68, form['first_name']", form['first_name'])
                print("line 69, gnum.first_name", g_num.first_name)
                print("line 70, form['last_name']", form['last_name'])
                print("line 71, gnum.last_name", g_num.last_name)
                print("line 72, form['email']", form['email'])
                print("line 73, g_num.email", g_num.email)

                # Check email address matches
                if (form['first_name'] == g_num.first_name) and (
                        form['last_name'] == g_num.last_name):
                    # Update Guest model
                    g_num.email = form['email']
                    email = g_num.email
                g_num.gift_chosen = True
                g_num.gift_name = 'Money'
                print(type(g_num.gift_value), type(gift_amount))
                g_num.gift_value += int(gift_amount)
                g_num.save()
            # Stripe setup
            amount = float(gift_amount)
            stripe_total = round(amount * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            request.session['save_info'] = 'save-info' in request.POST
            email = form['email']
            # if not email:
            #     messages.error(
            #         request, ('There was an error with your form. '
            #                   'Please double check your information.'))
            # else:
            donation_number = Checkout.objects.latest('date')
            print('line 105 donation_number', donation_number)
            return redirect(reverse(
                'checkout_success',
                args=[donation_number, email]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        guests = Guest.objects.filter(group_id=request.user)
        guest = ''
        for g in guests:
            if guest == '':
                guest = g

        form = CheckoutForm(instance=guest)           # contains guest details
        gift_amount = request.session['gift_amount']  # from session (contexts)
        amount = float(gift_amount)
        stripe_total = round(amount * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print('amount ', amount, 'gift_amount ', gift_amount)
    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing from your environment.')

    template = 'checkout/checkout.html'
    context = {
        'guest': guest,
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


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
        # 'form': form,

    }

    return render(request, template, context)
