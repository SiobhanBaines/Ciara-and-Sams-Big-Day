# Generated by Django 3.2.4 on 2021-07-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0012_guest_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='dessert',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='guest',
            name='main',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='guest',
            name='starter',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
