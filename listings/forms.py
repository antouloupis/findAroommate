from django import forms
from .models import Listing
from .municipalities import MUNICIPALITIES
import datetime

def current_year():
    return datetime.date.today().year

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = [
            'title', 'description', 'price', 'municipality', 'hidden', 'size', #primary fields
            'bathrooms', 'roommates', 'floor', 'build_year', 'pet', #secondary
            'own_room', 'garden', 'parking', 'elevator', 'smoking']  # tetartiary
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'ex. Room in Gaza with a view'}),
            'description': forms.Textarea(attrs={'rows':4, 'cols':15, 'class':'form-control','placeholder':'An insightful description...'}),
            'build_year': forms.NumberInput(attrs={'class': 'form-control', 'min': '1940', 'max': str(current_year() + 1)}),
            'hidden' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'own_room' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'garden' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'parking' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'elevator' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'smoking' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'roommates' : forms.NumberInput(attrs={'class': 'form-control','min': '0','max':'10'}),
            'floor' : forms.NumberInput(attrs={'class': 'form-control','min': '-2','max': '15'}),
            'bathrooms' : forms.NumberInput(attrs={'class': 'form-control','min': '1','max':'10'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control','min': '15','max':'5000'}),
            'size' : forms.NumberInput(attrs={'class': 'form-control','min': '0','max':'500'}),
            'pet' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }
        
