# Generated by Django 4.1.3 on 2022-11-29 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0009_rename_photogallery_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('board', models.CharField(blank=True, max_length=64, null=True)),
                ('skill_level', models.IntegerField(blank=True, choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Pro')], null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('home_spot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guide.surfspot')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visited_spots', models.ManyToManyField(blank=True, null=True, related_name='visited_spots', to='guide.surfspot')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('surfspot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.surfspot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
