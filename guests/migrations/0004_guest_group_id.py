# Generated by Django 3.2.4 on 2021-06-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20210610_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='group_id',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
