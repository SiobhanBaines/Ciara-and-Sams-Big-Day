# Generated by Django 3.2.4 on 2021-07-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0011_guest_special_diet'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='requirements',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]