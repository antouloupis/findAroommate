from django.db import models
from django.contrib.auth.models import User
from listing.models import Listing  
# Create your models here.
# user = models.ForeignKey(User, on_delete=models.CASCADE)  # Deletes saved listings if the user is deleted
# listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  # Deletes saved references if the listing is deleted
# saved_at = models.DateTimeField(auto_now_add=True)

# class Meta:
#     unique_together = ('user', 'listing')  # Prevent saving the same listing multiple times
