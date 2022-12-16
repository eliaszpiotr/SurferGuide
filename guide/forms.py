from django import forms
from django.core.exceptions import ValidationError
from .models import SurfSpot, Photo, Comment, UserInformation, Season, Temperature


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
            'best_season': forms.CheckboxSelectMultiple(),
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
            'best_season': 'Best seasons for surfing',
            'difficulty': 'Entry surfing level',
            'danger': 'Dangers on the spot',
            'temperature_in_spring': 'Temperature of water in spring',
            'temperature_in_summer': 'Temperature of water in summer',
            'temperature_in_fall': 'Temperature of water in fall',
            'temperature_in_winter': 'Temperature of water in winter',
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        continent = cleaned_data.get('continent')
        country = cleaned_data.get('country')
        location = cleaned_data.get('location')
        best_season = cleaned_data.get('best_season')
        difficulty = cleaned_data.get('difficulty')
        danger = cleaned_data.get('danger')
        temperature_in_spring = cleaned_data.get('temperature_in_spring')
        if temperature_in_spring > 30:
            raise ValidationError('Temperature in spring cannot be higher than 30°C')
        temperature_in_summer = cleaned_data.get('temperature_in_summer')
        if temperature_in_summer > 30:
            raise ValidationError('Temperature in summer cannot be higher than 30°C')
        temperature_in_fall = cleaned_data.get('temperature_in_fall')
        if temperature_in_fall > 30:
            raise ValidationError('Temperature in fall cannot be higher than 30°C')
        temperature_in_winter = cleaned_data.get('temperature_in_winter')
        if temperature_in_winter > 30:
            raise ValidationError('Temperature in winter cannot be higher than 30°C')
        if not name and not description and not continent and not country and not location and not best_season and not difficulty and not danger:
            raise ValidationError('You have to write something!')


class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = '__all__'

        widgets = {
            'temperature_in_spring': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature_in_summer': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature_in_fall': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature_in_winter': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'temperature_in_spring': 'Temperature of water in spring',
            'temperature_in_summer': 'Temperature of water in summer',
            'temperature_in_fall': 'Temperature of water in fall',
            'temperature_in_winter': 'Temperature of water in winter',
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
