# Generated by Django 4.1.3 on 2022-11-29 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0010_userinformation_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='avatar',
        ),
        migrations.AddField(
            model_name='surfspot',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='continent',
            field=models.CharField(blank=True, choices=[('AF', 'Africa'), ('AN', 'Antarctica'), ('AS', 'Asia'), ('EU', 'Europe'), ('NA', 'North America'), ('OC', 'Oceania'), ('SA', 'South America')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]