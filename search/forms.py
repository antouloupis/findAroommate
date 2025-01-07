from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from listings.municipalities import MUNICIPALITIES
from listings.models import Location

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
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    garden = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    parking = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    elevator = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    smoking = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    pet = forms.TypedChoiceField(
        choices=[('', 'Any'), ('True', 'Yes'), ('False', 'No')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # This is a Bootstrap class to style the dropdown
        })
    )

    price_min = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Minimum',
            'onchange':'validatePrice()',
            'oninput':'restrictToNumbers(this)'
        })
    )
    price_max = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Maximum',
            'onchange':'validatePrice()',
            'oninput':'restrictToNumbers(this)'
        })
    )

    bathrooms_min = forms.IntegerField(
        validators=[MaxValueValidator(20)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': ' Minimum',
            'oninput':'validateBathrooms(this)',
        }))

    size_min = forms.IntegerField(
        validators=[MinValueValidator(0),
        MaxValueValidator(5000)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Minimum',
            'oninput':'validateSize(this)',
        }))

    roommates_max = forms.IntegerField(
        validators=[MaxValueValidator(10)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Maximum',
            'oninput':'validateRoommates(this)'
        }))

    floor_min = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Minimum',
            'onchange':'validateFloor()',
            'oninput':'restrictToNumbers(this)'
        }))
    floor_max = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',  # Adding Bootstrap class for styling
            'placeholder': 'Maximum',
            'onchange':'validateFloor()',
            'oninput':'restrictToNumbers(this)'
        }))
