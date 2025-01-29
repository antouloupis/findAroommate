from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from listings.models import Location
from profiles.models import Profile

class FilterForm(forms.Form):

    area = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        required=False,
        empty_label="Select area",
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

    own_room = forms.ChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select' 
        })
    )

    garden = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select' 
        })
    )

    parking = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    elevator = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select' 
        })
    )

    smoking = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  
        })
    )

    pet = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select' 
        })
    )

    price_min = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Minimum',
            'onchange':'validatePrice()',
            'oninput':'restrictToNumbers(this)'
        })
    )
    price_max = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Maximum',
            'onchange':'validatePrice()',
            'oninput':'restrictToNumbers(this)'
        })
    )

    bathrooms_min = forms.IntegerField(
        validators=[MaxValueValidator(20)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': ' Minimum',
            'oninput':'validateBathrooms(this)',
        }))

    size_min = forms.IntegerField(
        validators=[MinValueValidator(0),
        MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Minimum',
            'oninput':'validateSize(this)',
        }))

    roommates_max = forms.IntegerField(
        validators=[MaxValueValidator(10)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Maximum',
            'oninput':'validateRoommates(this)'
        }))

    floor_min = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Minimum',
            'onchange':'validateFloor()',
            'oninput':'restrictToNumbers(this)'
        }))
    floor_max = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Maximum',
            'onchange':'validateFloor()',
            'oninput':'restrictToNumbers(this)'
        }))


class FilterUsersForm(forms.Form):

    area = forms.ModelChoiceField(
        queryset=Profile.objects.exclude(location__isnull=True).exclude(location__exact="").distinct('location'),
        required=False,
        empty_label="Select area",
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

    pet = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].label_from_instance = lambda obj: obj.location
