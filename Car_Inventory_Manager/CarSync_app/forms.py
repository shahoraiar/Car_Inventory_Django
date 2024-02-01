
from django import forms
from .models import CarModel

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'model', 'year', 'car_type']

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter car name'}))
    model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter car model'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter car year'}))
    
     
    

