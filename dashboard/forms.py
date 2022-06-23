from dataclasses import field
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['country', 'year', 'category', 'state', 'type']