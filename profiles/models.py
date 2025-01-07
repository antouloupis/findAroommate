from django.db import models
from account.models import CustomUser
from listings.municipalities import MUNICIPALITIES

class Profile(models.Model):
    GENDER_PREFERENCES = ['Men', 'Women', 'Any']
    AGE_RANGE = ['18-30','31-40','41-50','51-60','60+','Other']
    PET_CHOICES = ["I like them", "I dislike them", "I like them, and have one (that will stay with me)"]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    hidden = models.BooleanField(default=True)
    age = models.CharField(
        choices=[(choice, choice) for choice in AGE_RANGE], 
        max_length=6,
        default="Other",
    )
    bio = models.TextField(max_length=2500,blank=True, null=True)
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    pets = models.CharField(
        choices=[(choice, choice) for choice in PET_CHOICES], 
        max_length=50,
        default='I like them',
    )

    pref_gender = models.CharField(
        choices=[(choice, choice) for choice in GENDER_PREFERENCES], 
        max_length=20,
        default='Any',
    )

    email = models.EmailField(max_length=254,blank=True,null=True)

    phone = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}"