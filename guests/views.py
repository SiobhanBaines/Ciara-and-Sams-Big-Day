from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect
from .models import Guest

# import csv
import uuid
from django.contrib import messages


def all_guests(request):
    """ View a list of all guests """
    guests = Guest.objects.all()
    context = {
        'guests': guests,
    }
    return render(request, 'guests/guests.html', context)

# most of the code below was taken from pythoncircle.com


def upload_guest_list(request):
    """
    Upload CSV file containing list of guests into Django Guests model
    """
    print('guests views line 25 ')
    print(request.method)
    data = {}
    if request.method == 'POST':

        try:
            csv_file = request.FILES['guest_list_csv']
            print('guest views line31 ', csv_file)
            # check file is csv
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect(reverse('guests/guests.html'))

            # load csv into file
            file_data = csv_file.read().decode('utf-8')
            # split file into records
            lines = file_data.split('\n')

            for line in lines:
                # split line into fields seperated by comma
                fields = line.split(',')

                # create user id on change of postcode
                post_code = ''
                if post_code != fields[9]:
                    post_code == fields[9]
                    unique_code = uuid.uuid4().hex[:6].upper()
                    User.objects.create_user(
                        username=unique_code, password=fields[9].strip())

                guest = Guest(
                    guest_id=unique_code,
                    first_name=fields[1],
                    last_name=fields[2],
                    plus_one=fields[3],
                    address_line_1=fields[4],
                    address_line_2=fields[5],
                    city=fields[6],
                    county=fields[7],
                    country=fields[8],
                    postcode=fields[9],
                    email=fields[10],
                    phone_number=fields[11],
                    accepted='',
                    meal_chosen=False,
                    starter='',
                    main='',
                    dessert='',
                    gift_chosen=False,
                    gift_name='',
                    gift_value=0,
                )

                guest.save()
            
        except Exception as e:
            messages.error(request, 'Unable to upload file. '+repr(e))
            print('guest views line83 failed')
    return redirect(reverse('guest/upload_guest_list'))
