# Generated by Django 3.2.4 on 2021-07-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0013_auto_20210718_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
