# Generated by Django 4.1.3 on 2022-11-28 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_surfspot_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surfspot',
            name='is_verified',
        ),
    ]
