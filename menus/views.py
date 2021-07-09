from django.shortcuts import render, reverse, redirect, get_object_or_404
# from django.views import View
from django.http import HttpResponse
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Menu
# from django.contrib.auth.models import User
from .forms import MenuForm

import io
import csv
# import uuid


@login_required
def menus(request):
    """ View a list of all menus """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menus = Menu.objects.all()
    query = None

    # if request.GET:
    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(
    #                 request, "You didn't enter any search criteria.")
    #             return redirect(reverse('menus'))

    #         queries = Q(
    #             first_name__icontains=query) | Q(last_name__icontains=query)
    #         menus = menus.filter(queries)

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['menu_list_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)

        objs = []
        # post_code = ''
        for row in list_of_dict:
            # # create user id on change of postcode
            # if post_code != row['postcode']:
            #     post_code = row['postcode'].strip()
            #     unique_group_id = uuid.uuid4().hex[:6].upper()
            #     User.objects.create_user(
            #         username=unique_group_id, password=row['postcode'])
            objs.append(
                Menu(
                    # course=unique_group_id,
                    course=row['course'],
                    name=row['name'],
                    description=row['description'],
                    # address_line_1=row['address_line_1'],
                    # address_line_2=row['address_line_2'],
                    # city=row['city'],
                    # county=row['county'],
                    # country=row['country'],
                    # postcode=row['postcode'],
                    # email=row['email'],
                    # phone_number=row['telephone'],
                    # accepted='',
                    # meal_chosen=False,
                    # starter='',
                    # main='',
                    # dessert='',
                    # gift_chosen=False,
                    # gift_name='',
                    # gift_value=0,
                )
            )
        try:
            msg = Menu.objects.bulk_create(objs)
            # returnmsg = {"status_code": 200}
            messages.success(request, 'Imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('menus')

    context = {
        'menus': menus,
        'search_term': query,
    }

    return render(request, 'menus/menus.html', context)


# @login_required
# def menu_detail(request, menu_id):
#     """ View individual menu details """

#     menu = get_object_or_404(Menu, pk=menu_id)
#     context = {
#         'menu': menu,
#     }

#     return render(request, 'menus/menu_detail.html', context)


@login_required
def add_menu(request):
    """ Add menu to menu list """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            # save data from form into model
            menu = form.save()

            # get newly create model details
            menu.id
            # menu.group_id
            # menu.postcode

            # create unique code for group_id
            # menu.group_id = uuid.uuid4().hex[:6].upper()
            menu = form.save()

            # User login credentials
            # User.objects.create_user(
            #     username=menu.group_id, password=menu.postcode)

            messages.success(request, 'Successfully added a new menu')
            return redirect(reverse('menu_detail', args=[menu.id]))
        else:
            messages.error(request, 'Failed to add menu. \
                           Please check the information is valid')
    else:
        form = MenuForm()

    form = MenuForm()

    template = 'menus/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu(request, menu_id):
    """ Edit a menu """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the menu')
            return redirect(reverse('menu_detail', args=[menu.id]))
        else:
            messages.error(request, 'Failed to update menu. \
                           Please check the information is valid')
    else:
        form = MenuForm(instance=menu)
        messages.info(
            request, f'You are editing {menu.name}')

    template = 'menus/edit_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


@login_required
def delete_menu(request, menu_id):
    """ Delete a menu """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)
    menu_name = str(menu.name)
    menu.delete()
    form = MenuForm(instance=menu)
    messages.success(
        request, f'Menu {menu_name} deleted')
    return redirect(reverse('menus'))
