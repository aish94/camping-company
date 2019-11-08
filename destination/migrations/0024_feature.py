# Generated by Django 2.2.1 on 2019-11-01 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0023_destination_site_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_roading', models.BooleanField()),
                ('cycling', models.BooleanField()),
                ('toilet', models.BooleanField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.Destination')),
            ],
        ),
    ]
