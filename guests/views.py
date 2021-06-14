﻿from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Guest
from django.contrib.auth.models import User
from .forms import GuestForm

import io
import csv
import uuid


@login_required
def all_guests(request):
    """ View a list of all guests """

    guests = Guest.objects.all()
    query = None

    if request.GET:
        print(request)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                print(messages.error)
                return redirect(reverse('guests'))

            queries = Q(
                first_name__icontains=query) | Q(last_name__icontains=query)
            guests = guests.filter(queries)

    if request.method == "POST":
        print(request)
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['guest_list_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)

        objs = []
        post_code = ''
        for row in list_of_dict:
            # create user id on change of postcode
            # unique_guest_id = uuid.uuid4().hex[:6].upper()
            if post_code != row['postcode']:
                post_code = row['postcode'].strip()
                print(row['postcode'])
                print(post_code)
                unique_group_id = uuid.uuid4().hex[:6].upper()
                User.objects.create_user(
                    username=unique_group_id, password=row['postcode'])
                print(row['plus_one'])
            objs.append(
                Guest(
                    group_id=unique_group_id,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    plus_one=row['plus_one'],
                    address_line_1=row['address_line_1'],
                    address_line_2=row['address_line_2'],
                    city=row['city'],
                    county=row['county'],
                    country=row['country'],
                    postcode=row['postcode'],
                    email=row['email'],
                    phone_number=row['telephone'],
                    accepted='',
                    meal_chosen=False,
                    starter='',
                    main='',
                    dessert='',
                    gift_chosen=False,
                    gift_name='',
                    gift_value=0,
                )
            )
        print('line 53 obj ', objs)
        try:
            msg = Guest.objects.bulk_create(objs)
            print('line 83 msg ', msg)
            # returnmsg = {"status_code": 200}
            messages.error(request, 'imported successfully')
            print(messages.error)
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            print(messages.error)
            return HttpResponse(content=e, status=400)

        return redirect('guests')

    context = {
        'guests': guests,
        'search_term': query,
    }

    return render(request, 'guests/guests.html', context)


@login_required
def view_guest(request, guest_id):
    """ View individual guest details """

    guest = get_object_or_404(Guest, pk=guest_id)
    context = {
        'guest': guest,
    }

    return render(request, 'guests/view_guest.html', context)


def add_guest(request):
    """ Add guest to guest list """
    print('line 119 ', request.method)
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        print('line 122 form ', form, form.is_valid)
        if form.is_valid():
            guest = form.save()

            messages.success(request, 'Successfully added a new guest')
            print('line 127 ', messages.success)
            return redirect(reverse('view_guest', args=[guest.id]))
        else:
            messages.error(request, 'Failed to add guest. Please check the information is valid')
            print('line 127 ', messages.error)
    else:
        form = GuestForm()

    form = GuestForm()
    template = 'guests/add_guest.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_guest(request, guest_id):
    """ Edit a guest """
    print(request.method)
    guest = get_object_or_404(Guest, pk=guest_id)
    print('line 145 guest', guest)
    
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES, instance=guest)
        print('line 149 form ', form.is_valid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the guest')
            print('line 154 ', messages.success)
            return redirect(reverse('view_guest', args=[guest.id]))
        else:
            messages.error(request, 'Failed to add guest. Please check the information is valid')
            print('line 158 ', messages.error)
    else:
        form = GuestForm(instance=guest)
        messages.info(
            request, f'You are editing {guest.first_name} {guest.last_name}')
        print('line 163 ',messages.info)
    template = 'guests/edit_guest.html'
    context = {
        'form': form,
        'guest': guest,
    }

    return render(request, template, context)
