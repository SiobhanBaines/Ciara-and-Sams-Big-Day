from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
# from django.http import HttpResponse, JsonResponse
from django.views import View

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Guest
# from django.contrib.auth.models import User

import io
import csv
# import uuid


def all_guests(request):
    """ View a list of all guests """
    print('guests views line 13 ')
    guests = Guest.objects.all()
    print(guests)
    context = {
        'guests': guests,
    }
    print(context)
    return render(request, 'guests/all_guests.html', context)


class UploadGuestListView(View):

    @login_required
    def get(self, request):
            template_name = 'upload_guest_list.html'
            return render(request, template_name)


    @login_required
    def post(self, request):
        """
        Upload CSV file containing list of guests into Django Guests model
        """
        print('line 34 self, equest', request)
        user = request.user   # get the current login user details
        print('user', user)
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['guest_list_csv'].file)
        print('line 38 paramFile', paramFile)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        print('line 40 portfolio1 ', portfolio1)
        list_of_dict = list(portfolio1)
        print('line 42 list_of_dict ', list_of_dict)
        # create user id on change of postcode
        # post_code = ''
        # print('line 45 row(postcode) ', row['postcode'])
        # if post_code != row['postcode']:

        #     post_code == row['postcode']
        #     unique_code = uuid.uuid4().hex[:6].upper()
        #     User.objects.create_user(
        #         username=unique_code, password=row['postcode'].strip())
        # print('line 50 unique_code, password ', unique_code, password=row['postcode'].strip())
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
            returnmsg = {"status_code": 200}
            messages.error(request, 'imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}

        # return JsonResponse(returnmsg)
        # if request.method == 'POST':
        #     try:
        #         csv_file = request.FILES['guest_list_csv']
        #         print('guest views line33 ', csv_file)
        #         # check file is csv

        #         # print('line 35 csv_file.name.endswith', csv_file.name.endswith('.csv'))
        #         if csv_file.name.endswith('.csv'):
        #         # if not csv_file.name.endswith('.csv'):
        #             print('inside if statement line 37')
        #         #     messages.error(request, 'File is not CSV type')
        #         #     return redirect(reverse('all_guests'))

        #             print('line 40 csv_file.name.endswith', csv_file.name.endswith())
        #             # load csv into file
        #             file_data = csv_file.read().decode('utf-8')
        #             print('line 43 file_data', file_data)
        #             # split file into records
        #             lines = file_data.split('\n')
        #             print('line 46 lines', lines)
        #  print('line 87')

        return redirect(reverse('all_guests'))
