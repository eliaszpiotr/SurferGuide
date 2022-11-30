from django import forms
from django.core.exceptions import ValidationError

from .models import SurfSpot, Photo, Comment, UserInformation


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
    username = forms.CharField(max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               label='')
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               label='')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               label='')
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               label="")
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat password'}), label="")

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
            'text': forms.Textarea(
                attrs={'placeholder': 'Write your comment here...', 'rows': 3, 'class': 'form-control'}),
        }

        labels = {
            'text': '',
        }


class ProfileSettingsForm(forms.ModelForm):

    spots_queryset1 = SurfSpot.objects.order_by('continent')
    spots_queryset2 = SurfSpot.objects.order_by('continent')

    class Meta:
        model = UserInformation
        fields = ['country', 'continent', 'bio', 'home_spot', 'skill_level', 'board', 'achievements', 'visited_spots']

        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portugal'}),
            'continent': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Bio'}),
            'home_spot': forms.Select(attrs={'class': 'form-control'}),
            'skill_level': forms.Select(attrs={'class': 'form-control'}),
            'board': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your surfing board'}),
            'achievements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Achievements'}),
            'visited_spots': forms.SelectMultiple(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'bio': 'Write a short bio about yourself',
            'home_spot': 'Your home surf spot',
            'skill_level': 'Your surfing skills level',
            'board': 'Your surfing board',
            'achievements': 'Your achievements in surfing tournaments',
            'visited_spots': 'Spots you have visited',
        }

        ordering = {
            'home_spot': 'continent',
            'visited_spots': 'continent',
        }
