from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    photo = forms.ImageField()

    class Meta:
        model = Photo
        fields = ['title', 'photo']