from django.contrib.auth.models import AbstractUser
from django.db import models
from listings.models import Listing


class CustomUser(AbstractUser):
    favorite_listings = models.ManyToManyField(Listing, related_name='saved_by', blank=True)
    is_email_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=20, unique=True)



class Message(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, blank=True)  # Reference to the listing
    content = models.TextField(max_length=500)
    sender = models.ForeignKey(CustomUser, related_name='sent_messages',on_delete=models.SET_NULL,null=True, blank=True )
    recipient = models.ForeignKey(CustomUser, related_name='received_messages',on_delete=models.SET_NULL,null=True, blank=True )
    date = models.DateTimeField(auto_now_add=True)
    sender_deleted = models.BooleanField(default=False)
    recipient_deleted = models.BooleanField(default=False) 


    def __str__(self):
        return f"Message from {self.sender} for {self.listing}"