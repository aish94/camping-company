# Generated by Django 2.2.1 on 2019-10-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genie', '0003_auto_20191018_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoid',
            name='id1',
            field=models.ImageField(blank=True, upload_to='genie/photo_id'),
        ),
        migrations.AlterField(
            model_name='photoid',
            name='id2',
            field=models.ImageField(blank=True, upload_to='genie/photo_id'),
        ),
        migrations.AlterField(
            model_name='photoid',
            name='id3',
            field=models.ImageField(blank=True, upload_to='genie/photo_id'),
        ),
        migrations.AlterField(
            model_name='photoid',
            name='id4',
            field=models.ImageField(blank=True, upload_to='genie/photo_id'),
        ),
        migrations.AlterField(
            model_name='photoid',
            name='id5',
            field=models.ImageField(blank=True, upload_to='genie/photo_id'),
        ),
    ]