# Generated by Django 2.2.1 on 2019-11-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0043_auto_20191121_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='total_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]