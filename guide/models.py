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
    country = models.CharField(max_length=64, blank=True, null=True)

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
        NORTH = 'N', 'North'
        NORTH_EAST = 'NE', 'North-East'
        EAST = 'E', 'East'
        SOUTH_EAST = 'SE', 'South-East'
        SOUTH = 'S', 'South'
        SOUTH_WEST = 'SW', 'South-West'
        WEST = 'W', 'West'
        NORTH_WEST = 'NW', 'North-West'

    best_wind = models.CharField(max_length=13, choices=Wind.choices)

    class WaveDirection(models.TextChoices):
        L = 'L', 'Left'
        R = 'R', 'Right'
        B = 'B', 'Both'

    wave_direction = models.CharField(max_length=1, choices=WaveDirection.choices)

    class SpotType(models.TextChoices):
        B = 'B', 'Beach break'
        R = 'R', 'Reef break'
        P = 'P', 'Point break'
        O = 'O', 'Other break'

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

    best_season = models.ManyToManyField('Season', blank=True)

    temperature_in_spring = models.IntegerField(blank=True, null=True)
    temperature_in_summer = models.IntegerField(blank=True, null=True)
    temperature_in_fall = models.IntegerField(blank=True, null=True)
    temperature_in_winter = models.IntegerField(blank=True, null=True)

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


class Season(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Photo(models.Model):
    surfspot = models.ForeignKey(SurfSpot, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.surfspot.name} image{self.id}'


class Comment(models.Model):
    surfspot = models.ForeignKey(SurfSpot, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.surfspot.name} comment'


class UserInformation(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    country = models.CharField(max_length=64, blank=True, null=True)
    continent = models.CharField(choices=SurfSpot.Continent.choices, max_length=2, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    home_spot = models.ForeignKey(SurfSpot, on_delete=models.SET_NULL, blank=True, null=True)
    board = models.CharField(max_length=64, blank=True, null=True)

    class SkillLevel(models.IntegerChoices):
        BEGINNER = 1
        INTERMEDIATE = 2
        ADVANCED = 3
        PRO = 4

    skill_level = models.IntegerField(choices=SkillLevel.choices, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    visited_spots = models.ManyToManyField(SurfSpot, blank=True, null=True, related_name='visited_spots')

    # FUTURE FEATURES
    # friends = models.ManyToManyField('auth.User', blank=True, null=True)

    # class RankOnSite(models.IntegerChoices):
    #     KOOK = 1
    #     LOCAL_GUIDE = 3
    #     LEGENDARY_SURFER = 4
    #
    # rank = models.IntegerField(choices=RankOnSite.choices, blank=True, null=True, default=1)

    def __str__(self):
        return f'{self.user.username} information'
