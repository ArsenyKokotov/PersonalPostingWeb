from django import forms
from django.forms import ModelForm
from . models import *

class CreateDescription(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['txt_description', 'profile_pic']
        labels = { 
            'txt_description': 'Describe yourself',
            'profile_pic': 'Choose your profile pic ', 
        }

class CreateGallery(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['txt', 'new_file']
        labels = {
            'txt': 'Describe your file',
            'new_file': 'Choose your file '
        }