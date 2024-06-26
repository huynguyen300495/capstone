# Generated by Django 5.0.4 on 2024-04-13 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTable',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.SmallIntegerField()),
                ('booking_date', models.DateField(default=datetime.date(2024, 4, 13))),
            ],
            options={
                'db_table': 'BookingTable',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('inventory', models.IntegerField()),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
    ]
