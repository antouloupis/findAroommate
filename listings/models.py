from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .municipalities import MUNICIPALITIES
import datetime
# Create your models here.

class Listing(models.Model):
    current_year = datetime.date.today().year  # Get the current year
    title = models.CharField(max_length=50)
    description = models.TextField() #put a max length for description here
    municipality = models.CharField(
        max_length=100,
        choices=[(option, option) for option in MUNICIPALITIES],
        default=None,
        )
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(15),MaxValueValidator(5000)]  # Set a maximum value if needed
    )
    size = models.PositiveIntegerField(validators=[MinValueValidator(15),MaxValueValidator(500)])
    date_listed = models.DateTimeField(auto_now_add=True) #save date on creation
    hidden = models.BooleanField(default=False)
    #Details
    bathrooms = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], null = True,blank=True)
    roommates = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], null = True,blank=True)
    floor = models.SmallIntegerField(validators=[MaxValueValidator(15),MinValueValidator(-2)], null = True,blank=True)
    pet = models.BooleanField(null = True,blank=True)
    #Extra details
    own_room = models.BooleanField(null = True,blank=True)
    garden = models.BooleanField(null = True,blank=True)
    parking = models.BooleanField(null = True,blank=True)
    elevator = models.BooleanField(null = True,blank=True)
    smoking = models.BooleanField(null = True,blank=True)
    build_year = models.SmallIntegerField(null = True,blank=True,
    validators=[
        MaxValueValidator((current_year + 1)),
        MinValueValidator(1940)],
        )

    
    def __str__(self):
        return self.title

