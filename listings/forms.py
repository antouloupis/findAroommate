from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'location', 'price', 'hidden']  # Fields you want in the form
        
        # Add custom widgets if needed, like for the radio button
        widgets = {
            'hidden': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        }