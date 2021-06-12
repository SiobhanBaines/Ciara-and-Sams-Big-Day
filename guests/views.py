from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Guest
from django.contrib.auth.models import User

import io
import csv
import uuid


@login_required
def all_guests(request):
    """ View a list of all guests """

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
                print(row['postcode'])
                print(post_code)
                # last_name = row['last_name']
                # new_password = post_code + last_name.upper()
                # print(new_password)
                unique_code = uuid.uuid4().hex[:6].upper()
                User.objects.create_user(
                    username=unique_code, password=row['postcode'])
                print(row['plus_one'])
            objs.append(
                Guest(
                    guest_id=unique_code,
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
            return redirect(reverse('all_guests'))
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('all_guests')

    guests = Guest.objects.all()
    context = {
        'guests': guests,
    }

    return render(request, 'guests/all_guests.html', context)
