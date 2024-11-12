from django import forms
from .models import Asset
from .models import Screen

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['file_name', 'file_url', 'file_type']
        labels = {
            'file_name': 'File Name',
            'file_url': 'File URL',
            'file_type': 'File Type'
        }
        widgets = {
            'file_name': forms.TextInput(attrs={'class': 'form-control'}),
            'file_url': forms.URLInput(attrs={'class': 'form-control'}),
            'file_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ['screen_name', 'screen_location']
        labels = {
            'screen_name': 'Screen Name',
            'screen_location': 'Screen Location'
        }
        widgets = {
            'screen_name': forms.TextInput(attrs={'class': 'form-control'}),
            'screen_location': forms.TextInput(attrs={'class': 'form-control'}),
        }