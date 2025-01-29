from django.db import models
from account.models import CustomUser

class Profile(models.Model):
    AGE_RANGE = [
        ('18-30', '18-30'),
        ('31-40', '31-40'),
        ('41-50', '41-50'),
        ('51-60', '51-60'),
        ('60+', '60+'),
        ('Other', 'Other')
        ]
    PET_CHOICES = [
        ('True','I like them'),
        ('False', 'I dislike them'),
        ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    hidden = models.BooleanField(default=True)
    age = models.CharField(
        choices=AGE_RANGE, 
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
        choices=PET_CHOICES, 
        max_length=50,
        default='True',
    )

    
    email = models.EmailField(max_length=254,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}"