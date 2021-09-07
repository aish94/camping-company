# Generated by Django 2.2.1 on 2021-09-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0045_auto_20191124_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=40, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('activity', models.CharField(blank=True, max_length=256, null=True)),
                ('quotation', models.CharField(blank=True, max_length=256, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.CharField(blank=True, max_length=256, null=True)),
                ('group_size', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to='experiences')),
                ('image2', models.ImageField(blank=True, upload_to='experiences')),
                ('image3', models.ImageField(blank=True, upload_to='experiences')),
                ('image4', models.ImageField(blank=True, upload_to='experiences')),
                ('image5', models.ImageField(blank=True, upload_to='experiences')),
            ],
        ),
    ]
