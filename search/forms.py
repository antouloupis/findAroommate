from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from listings.municipalities import MUNICIPALITIES

class FilterForm(forms.Form):  # Using forms.Form, not ModelForm
    municipality = forms.ChoiceField(
        choices=[(option, option) for option in MUNICIPALITIES],
        required=False
    )

    own_room = forms.BooleanField(required=False)
    garden = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    smoking = forms.BooleanField(required=False)
    pet = forms.BooleanField(required=False)

    price_min = forms.IntegerField(
        validators=[
            MinValueValidator(0),  # Ensure the value is not negative
            MaxValueValidator(5000)  # Ensure the value does not exceed 5000
        ],
        required=False
    )
    
    price_max = forms.IntegerField(
        validators=[
            MinValueValidator(0),  # Ensure the value is not negative
            MaxValueValidator(5000)  # Ensure the value does not exceed 5000
        ],
        required=False
    )

        
    bathrooms_min = forms.IntegerField(
        validators=[MaxValueValidator(20)],
        required=False
    )

    bathrooms_max = forms.IntegerField(
        validators=[MaxValueValidator(20)],
        required=False
    )   
    
    size_min = forms.IntegerField(
        validators=[
            MinValueValidator(0),  # Ensure the value is not negative
            MaxValueValidator(5000)
        ],
        required=False
    )
    
    size_max = forms.IntegerField(
        validators=[
            MinValueValidator(0),  # Ensure the value is not negative
            MaxValueValidator(5000)
        ],
        required=False
    )
        
    roommates_min = forms.IntegerField(
        validators=[MaxValueValidator(10)],
        required=False
    )

    roommates_max = forms.IntegerField(
        validators=[MaxValueValidator(10)],
        required=False
    )

    floor_min = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False
    )
    
    floor_max = forms.IntegerField(
        validators=[MaxValueValidator(15)],
        required=False
    )
    
            
    def clean(self):
        cleaned_data = super().clean()  # Call the parent clean method
        
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')
        
        # Check if both price_min and price_max are provided
        if price_min is not None and price_max is not None:
            if price_min > price_max:
                raise forms.ValidationError("Minimum price cannot be greater than maximum price.")
        
        return cleaned_data  # Return the cleaned data   
