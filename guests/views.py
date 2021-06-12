from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from .models import Guest
# from django.contrib.auth.models import User

import io
import csv
# import uuid


def all_guests(request):
    """ View a list of all guests """

    if request.method == "POST":
        print('line 37 - post process')
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['guest_list_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        print('line 42 list_of_dict ', list_of_dict)

        objs = [
            Guest(
                        guest_id='',
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
            for row in list_of_dict
        ]
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
    print(context)

    return render(request, 'guests/all_guests.html', context)
