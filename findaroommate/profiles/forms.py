from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    
    location = forms.CharField(widget=forms.HiddenInput(attrs={'id':'location','value':'Athens'}))

    class Meta:
        model = Profile
        fields = ['hidden', 'age', 'bio', 'location', 'pets', 'email','phone',]
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 13,'placeholder': 'Write some information about yourself...'}),
            'age': forms.Select(attrs={'class': 'form-select'}),
            'hidden': forms.CheckboxInput(attrs={'class': 'form-check-input my-auto p-3'}),
            'pets': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'hidden': 'Hide profile from search results?',
            'email':'Contact email',
            'phone':'Contact phone',
            'age':'Age range',
        }
