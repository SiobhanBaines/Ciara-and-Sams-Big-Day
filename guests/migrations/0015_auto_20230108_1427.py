# Generated by Django 3.2.4 on 2023-01-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0014_alter_guest_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='plus_one_first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='plus_one_last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
