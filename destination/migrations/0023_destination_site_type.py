# Generated by Django 2.2.1 on 2019-10-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0022_auto_20191028_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='site_type',
            field=models.CharField(default='asd', max_length=64),
            preserve_default=False,
        ),
    ]