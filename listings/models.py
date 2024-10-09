from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() #put a max length for description here
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField(
        validators=[MaxValueValidator(5000)]  # Set a maximum value if needed
    )
    date_listed = models.DateTimeField(auto_now_add=True) #save date on creation
    hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title