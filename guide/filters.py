import django_filters
from django.contrib.auth.models import User
from guide.models import SurfSpot


class SurfSpotFilter(django_filters.FilterSet):
    class Meta:
        model = SurfSpot
        fields = ['continent', 'country', 'difficulty', 'swell_size', 'crowd']


class SurfersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']



