from django import forms
from django.forms import ModelForm

from .models import *
class Noteform(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:
        model = Note
        fields = '__all__'
