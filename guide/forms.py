from django import forms
from django.core.exceptions import ValidationError

from .models import SurfSpot, Photo, UserInformation


class SurfSpotForm(forms.ModelForm):
    class Meta:
        model = SurfSpot
        fields = "__all__"


# class DangerForm(forms.ModelForm):
#     class Meta:
#         model = Danger
#         fields = "__all__"


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



