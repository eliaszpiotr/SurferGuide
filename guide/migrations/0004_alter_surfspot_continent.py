# Generated by Django 4.1.3 on 2022-11-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_alter_surfspot_best_wind_alter_surfspot_swell_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfspot',
            name='continent',
            field=models.CharField(choices=[('Africa', 'Africa'), ('Antarctica', 'Antarctica'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('Oceania', 'Oceania'), ('South America', 'South America')], max_length=16),
        ),
    ]
