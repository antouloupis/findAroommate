from django.contrib.auth.models import AbstractUser
from django.db import models
from listings.models import Listing  # Import your Listing model
from django.core.exceptions import ValidationError
import re

class CustomUser(AbstractUser):
    favorite_listings = models.ManyToManyField(Listing, related_name='saved_by', blank=True)
    #for users to have a favorite list
    
    # Set the maximum length for the username
    username = models.CharField(max_length=20, unique=True)

    def clean(self):
        super().clean()  # Call the parent's clean method

        # Check if username starts with a hyphen or underscore
        if self.username.startswith(('-', '_')):
            raise ValidationError('Username must not start with a hyphen or underscore.')

        # Regex to check for invalid characters (allow alphanumeric, _, and -)
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$', self.username):
            raise ValidationError('Username cannot have special characters except for dash(-) and underscore(_).')

        # Check for max length
        if len(self.username) > 20:
            raise ValidationError('Username must not exceed 20 characters.')