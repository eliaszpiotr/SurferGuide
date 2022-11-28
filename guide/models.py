from django.db import models


# Create your models here.
from django.urls import reverse


class Danger(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class SurfSpot(models.Model):
    # main info
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)

    class Continent(models.TextChoices):
        AFRICA = 'AF', 'Africa'
        ANTARCTICA = 'AN', 'Antarctica'
        ASIA = 'AS', 'Asia'
        EUROPE = 'EU', 'Europe'
        NORTH_AMERICA = 'NA', 'North America'
        OCEANIA = 'OC', 'Oceania'
        SOUTH_AMERICA = 'SA', 'South America'

    continent = models.CharField(choices=Continent.choices, max_length=2)

    # conditions
    class Wind(models.TextChoices):
        N = 'N', 'North'
        NE = 'NE', 'North East'
        E = 'E', 'East'
        SE = 'SE', 'South East'
        S = 'S', 'South'
        SW = 'SW', 'South West'
        W = 'W', 'West'
        NW = 'NW', 'North West'

    best_wind = models.CharField(max_length=2, choices=Wind.choices)

    class WaveDirection(models.TextChoices):
        L = 'L', 'Left'
        R = 'R', 'Right'
        B = 'B', 'Both'

    wave_direction = models.CharField(max_length=1, choices=WaveDirection.choices, default='B')

    class SpotType(models.TextChoices):
        B = 'B', 'Beach'
        R = 'R', 'Reef'
        P = 'P', 'Point'
        H = 'H', 'Headland'
        C = 'C', 'Cove'
        L = 'L', 'Lagoon'
        O = 'O', 'Other'

    spot_type = models.CharField(max_length=1, choices=SpotType.choices)

    class WaveType(models.TextChoices):
        G = 'G', 'Gentle'
        M = 'M', 'Moderate'
        H = 'H', 'Heavy'
        E = 'E', 'Extreme'

    wave_type = models.CharField(max_length=1, choices=WaveType.choices)

    class WaveHeight(models.IntegerChoices):
        SMALL = 1, '1-3 ft.'
        MEDIUM = 2, '3-6 ft.'
        LARGE = 3, '6-9 ft.'
        HUGE = 4, '9-12 ft.'
        MASSIVE = 5, '12+ ft.'
        SUPERMASSIVE = 6, '20+ ft.'

    swell_size = models.IntegerField(choices=WaveHeight.choices)

    # additional info

    class Crowd(models.IntegerChoices):
        EMPTY = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4
        FULL = 5

    crowd = models.IntegerField(choices=Crowd.choices)

    class Seasons(models.IntegerChoices):
        WINTER = 1
        SPRING = 2
        SUMMER = 3
        AUTUMN = 4

    best_season = models.IntegerField(choices=Seasons.choices)

    class Difficulty(models.IntegerChoices):
        BEGINNER = 1
        INTERMEDIATE = 2
        ADVANCED = 3
        PRO = 4

    difficulty = models.IntegerField(choices=Difficulty.choices)

    danger = models.ManyToManyField(Danger, blank=True, null=True)

    def __str__(self):
        return f'{self.name}, {self.continent}'

    def get_absolute_url(self):
        return reverse('spot', kwargs={'pk': self.pk})


# class PhotoGallery(models.Model):
#     surfspot = models.ForeignKey(SurfSpot, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.surfspot.name} image'
