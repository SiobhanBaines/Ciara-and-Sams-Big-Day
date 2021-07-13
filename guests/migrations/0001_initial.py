# Generated by Django 3.2.4 on 2021-06-10 07:47

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('guest_id', models.CharField(blank=True, max_length=6)),
                ('first_name', models.CharField(blank=False, max_length=50)),
                ('last_name', models.CharField(blank=False, max_length=50)),
                ('plus_one', models.BooleanField(default=False)),
                ('address_line_1', models.CharField(
                    blank=True, max_length=80)),
                ('address_line_2', models.CharField(
                    blank=True, max_length=80)),
                ('city', models.CharField(max_length=40, blank=True, )),
                ('county', models.CharField(blank=True, max_length=80)),
                ('country', models.CharField(max_length=40)),
                ('country_code', django_countries.fields.CountryField(
                    blank=True, max_length=2, null=True)),
                ('postcode', models.CharField(blank=False, max_length=20)),
                ('accepted', models.CharField(blank=True, max_length=1)),
                ('meal_chosen', models.BooleanField(default=False)),
                ('starter', models.CharField(blank=True, max_length=80)),
                ('main', models.CharField(blank=True, max_length=80)),
                ('dessert', models.CharField(blank=True, max_length=80)),
                ('gift_chosen', models.BooleanField(default=False)),
                ('gift_name', models.CharField(blank=True, max_length=254)),
                ('gift_value', models.DecimalField(
                    decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
    ]
