from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Menu
from guests.models import Guest
from .forms import MenuForm, GuestForm

import io
import csv


@login_required
def menus(request):
    """ View a list of all menus """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menus = Menu.objects.all()

    if request.method == "POST":
        # Handle request CSV file
        paramFile = io.TextIOWrapper(request.FILES['menu_csv'].file)
        # Read te POST request file and convert into DICT
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)

        objs = []
        for row in list_of_dict:
            objs.append(
                Menu(
                    course=row['course'],
                    menu_item=row['menu_item'],
                )
            )
        try:
            Menu.objects.bulk_create(objs)
            messages.success(request, 'Imported successfully')
        except Exception as e:
            messages.error(request, 'Error While Importing Data: ', e)
            return HttpResponse(content=e, status=400)

        return redirect('menus')

    form = MenuForm()
    context = {
        'menus': menus,
        'form': form,
    }

    return render(request, 'menus/menus.html', context)


@login_required
def display_menu(request):
    """ View of menu details """

    courses = []
    menus = Menu.objects.all().order_by('-course')
    for menu in menus:
        if menu.course not in courses:
            courses.append(menu.course)

    print(courses)

    form = MenuForm()
    context = {
        'courses': courses,
        'menus': menus,
        'form': form,
    }

    return render(request, 'menus/display_menu.html', context)


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
            menu = form.save()

            messages.success(request, 'Successfully added a new menu')
            return redirect(reverse('menus'))
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
    """ Edit an Event """
    if not request.user.is_superuser or not request.user.is_staff:
        messages.error(request, 'Sorry, only the bride and groom can do that.')
        return redirect(reverse('home'))

    menu = get_object_or_404(Menu, pk=menu_id)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the menu')
            return redirect(reverse('menus'))
        else:
            messages.error(request, 'Failed to update menu. \
                           Please check the information is valid')
    else:
        form = MenuForm(instance=menu)
        messages.info(
            request, 'You are editing an event')

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
    menu.delete()
    # form = MenuForm(instance=menu)
    messages.success(
        request, 'Menu event deleted')
    return redirect(reverse('menus'))


@login_required
def menu_selection(request):
    """ View of menu details """

    if request.method == 'POST':
        form = dict(request.POST)
        # loop through form to get details of each guest in the family group
        for num in range(len(form['id'])):
            guest_id = form['id'][num]
            guest = get_object_or_404(Guest, id=guest_id)
            guest.starter = form['starter'][num]
            guest.main = form['main'][num]
            guest.dessert = form['dessert'][num]
            guest.requirements = form['requirements'][num]
            # Set the special_diet flag to True or False
            if guest.requirements:
                guest.special_diet = True

            guest.meal_chosen = True
            guest.save()
            guest_form = form
            messages.info(request, 'Thank you for selecting you \
                meal preference.')
            return redirect(reverse('display_menu'))
    else:

        guest_form = GuestForm()

    guests = Guest.objects.filter(group_id=request.user)
    menus = Menu.objects.all()
    s = 0
    m = 0
    d = 0
    for menu in menus:
        if menu.course == "starter":
            s += 1
            if s == 1:
                starter_1 = str(menu.menu_item)
            else:
                starter_2 = str(menu.menu_item)
        elif menu.course == 'main':
            m += 1
            if m == 1:
                main_1 = str(menu.menu_item)
            else:
                main_2 = str(menu.menu_item)
        elif menu.course == 'dessert':
            d += 1
            if d == 1:
                dessert_1 = str(menu.menu_item)
            else:
                dessert_2 = str(menu.menu_item)

    context = {
        'menus': menus,
        'guests': guests,
        'guest_form': guest_form,
        'starter_1': starter_1,
        'starter_2': starter_2,
        'main_1': main_1,
        'main_2': main_2,
        'dessert_1': dessert_1,
        'dessert_2': dessert_2
    }

    return render(request, 'menus/menu_selection.html', context)
