# Generated by Django 4.1.3 on 2022-11-30 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0014_remove_surfspot_map_url_surfspot_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surfspot',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='surfspot',
            name='longitude',
        ),
    ]