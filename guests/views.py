from django.shortcuts import (
    render, reverse, redirect, get_object_or_404)
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
def guests(request):
    """ View a list of all guests """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    guests = Guest.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'group_id':
                sortkey = 'group_id'
            if sortkey == 'first_name':
                sortkey = 'first_name'
            if sortkey == 'last_name':
                sortkey = 'last_name'
            if sortkey == 'accepted':
                sortkey = 'accepted'
            if sortkey == 'meal_chosen':
                sortkey = 'meal_chosen'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            guests = guests.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                return redirect(reverse('guests'))

            queries = Q(
                first_name__icontains=query) | Q(last_name__icontains=query)
            guests = guests.filter(queries)

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['guest_list_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)

        objs = []
        post_code = ''
        for row in list_of_dict:
            # create user id on change of postcode
            if post_code != row['postcode']:
                post_code = row['postcode'].strip()
                unique_group_id = uuid.uuid4().hex[:6].upper()
                User.objects.create_user(
                    username=unique_group_id, password=row['postcode'])
            # Most people will use Excel to create the CSV file which puts True
            #   in Capitals which is not the same as a boolean True
            if row['plus_one'] == "TRUE":
                row_plus_one = True
            else:
                row_plus_one = False

            objs.append(
                Guest(
                    group_id=unique_group_id,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    plus_one=row_plus_one,
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
        try:
            Guest.objects.bulk_create(objs)
            messages.success(request, 'Imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('guests')

    current_sorting = f'{sort}_{direction}'

    context = {
        'guests': guests,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'guests/guests.html', context)


@login_required
def guest_detail(request, guest_id):
    """ View individual guest details """

    guest = get_object_or_404(Guest, pk=guest_id)
    context = {
        'guest': guest,
    }

    return render(request, 'guests/guest_detail.html', context)


@login_required
def add_guest(request):
    """ Add guest to guest list """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            guest = form.save()

            # get newly create model details
            guest.id
            guest.group_id
            guest.postcode

            # create unique code for group_id
            guest.group_id = uuid.uuid4().hex[:6].upper()
            guest = form.save()

            # User login credentials
            User.objects.create_user(
                username=guest.group_id, password=guest.postcode)

            messages.success(request, 'Successfully added a new guest')
            return redirect(reverse('guest_detail', args=[guest.id]))
        else:
            messages.error(request, 'Failed to add guest. \
                           Please check the information is valid')
    else:
        form = GuestForm()

    form = GuestForm()

    template = 'guests/add_guest.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_guest(request, guest_id):
    """ Edit a guest """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    guest = get_object_or_404(Guest, pk=guest_id)

    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the guest')
            return redirect(reverse('guest_detail', args=[guest.id]))
        else:
            messages.error(request, 'Failed to update guest. \
                           Please check the information is valid')
    else:
        form = GuestForm(instance=guest)
        messages.info(
            request, f'You are editing {guest.first_name} {guest.last_name}')

    template = 'guests/edit_guest.html'
    context = {
        'form': form,
        'guest': guest,
    }

    return render(request, template, context)


@login_required
def delete_guest(request, guest_id):
    """ Delete a guest """
    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    guest = get_object_or_404(Guest, pk=guest_id)
    guest_name = str(guest.first_name) + ' ' + str(guest.last_name)
    guest.delete()

    messages.success(
        request, f'Guest {guest_name} deleted')
    return redirect(reverse('guests'))
