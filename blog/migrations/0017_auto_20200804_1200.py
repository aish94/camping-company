# Generated by Django 2.2.1 on 2020-08-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_eventcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcart',
            old_name='person_tent',
            new_name='person_roof',
        ),
    ]
