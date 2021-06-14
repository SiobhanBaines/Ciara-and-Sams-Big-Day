from django.shortcuts import render, reverse, redirect, get_object_or_404
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
                messages.error(request, "You didn't enter any search criteria.")
                return redirect(reverse('guests'))

            queries = Q(first_name__icontains=query) | Q(last_name__icontains=query)
            print(queries)
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
            unique_guest_id = uuid.uuid4().hex[:6].upper()
            if post_code != row['postcode']:
                post_code = row['postcode'].strip()
                print(row['postcode'])
                print(post_code)
                # last_name = row['last_name']
                # new_password = post_code + last_name.upper()
                # print(new_password)
                unique_group_id = uuid.uuid4().hex[:6].upper()
                User.objects.create_user(
                    username=unique_group_id, password=row['postcode'])
                print(row['plus_one'])
            objs.append(
                Guest(
                    guest_id=unique_guest_id,
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
            return redirect(reverse('guests'))
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
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
    form = GuestForm()
    template = 'guests/add_guest.html'
    context = {
        'form': form,
    }

    return render(request, template, context)