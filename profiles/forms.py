from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    
    location = forms.CharField(widget=forms.HiddenInput(attrs={'id':'location','value':'Athina'}))

    class Meta:
        model = Profile
        fields = ['hidden', 'age', 'bio', 'location', 'pets', 'pref_gender','email','phone',]
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 6,'placeholder': 'Write some information about yourself...'}),
            'age': forms.Select(attrs={'class': 'form-select'}),
            'municipality': forms.Select(attrs={'class': 'form-select'}),
            'pref_gender': forms.Select(attrs={'class': 'form-select'}),
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
            'pref_gender':'I prefer to live with',
        }
