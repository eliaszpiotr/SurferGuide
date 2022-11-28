from django import forms
from .models import SurfSpot, Danger


class SurfSpotForm(forms.ModelForm):
    class Meta:
        model = SurfSpot
        fields = "__all__"


class DangerForm(forms.ModelForm):
    class Meta:
        model = Danger
        fields = "__all__"
