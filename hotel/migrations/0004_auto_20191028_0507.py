# Generated by Django 2.2.1 on 2019-10-28 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_hotel_slug'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='hotel',
            table='hotels',
        ),
    ]
