# Generated by Django 2.2.1 on 2021-10-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0007_auto_20191107_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='air_mattress',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
