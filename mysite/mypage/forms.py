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
        fields = ['name', 'txt', 'new_file']
        labels = {
            'name': 'Name your file',
            'txt': 'Describe your file',
            'new_file': 'Choose your file '
        }

class DeleteNamedFile(forms.Form):
    name = forms.CharField(label="Input name of file you want to delete ", max_length=20)