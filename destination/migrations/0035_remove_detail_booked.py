# Generated by Django 2.2.1 on 2019-11-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0034_remove_destination_cc_higlight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='booked',
        ),
    ]
