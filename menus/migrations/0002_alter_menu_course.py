# Generated by Django 3.2.4 on 2021-07-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='course',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
