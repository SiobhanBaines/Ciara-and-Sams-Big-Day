# Generated by Django 3.2.4 on 2021-06-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('selected', models.BooleanField(default=False)),
                ('supplier_link', models.CharField(
                    blank=True, max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(blank=True, max_length=1024)),
                ('image', models.ImageField(
                    blank=True, null=True, upload_to='')),
            ],
        ),
    ]
