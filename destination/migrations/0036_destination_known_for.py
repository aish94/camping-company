# Generated by Django 2.2.1 on 2019-11-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0035_remove_detail_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='known_for',
            field=models.CharField(default='ASD', max_length=128),
            preserve_default=False,
        ),
    ]