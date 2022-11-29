from django import forms
from django.core.exceptions import ValidationError

from .models import SurfSpot, Photo, Comment


class SurfSpotForm(forms.ModelForm):
    class Meta:
        model = SurfSpot
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surf Spot Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'continent': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lisbon'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portugal'}),
            'best_season': forms.Select(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'best_wind': forms.Select(attrs={'class': 'form-control'}),
            'wave_direction': forms.Select(attrs={'class': 'form-control'}),
            'spot_type': forms.Select(attrs={'class': 'form-control'}),
            'wave_type': forms.Select(attrs={'class': 'form-control'}),
            'swell_size': forms.Select(attrs={'class': 'form-control'}),
            'crowd': forms.Select(attrs={'class': 'form-control'}),
            'danger': forms.CheckboxSelectMultiple(),
        }

        labels = {
            'name': 'Name of the surf spot',
            'description': 'Description',
            'continent': 'Continent',
            'country': 'Country',
            'location': 'City',
            'best_season': 'Best season for surfing',
            'difficulty': 'Entry surfing level',
            'danger': 'Dangers on the spot',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput, label="Repeat password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            raise ValidationError("Passwords are not the same!")
        return cleaned_data


class AddPhotoForm(forms.Form):
    class Meta:
        model = Photo
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={'multiple': False, 'class': 'form-control-file'}),
        }


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment here...', 'rows': 3, 'class': 'form-control'}),
        }

        labels = {
            'text': '',
        }
