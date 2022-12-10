import django_filters
from guide.models import SurfSpot


class SurfSpotFilter(django_filters.FilterSet):
    class Meta:
        model = SurfSpot
        fields = ['continent', 'country', 'difficulty', 'swell_size', 'crowd']



