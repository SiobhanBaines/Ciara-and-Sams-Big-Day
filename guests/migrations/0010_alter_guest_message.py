# Generated by Django 3.2.4 on 2021-06-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_auto_20210620_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='message',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
