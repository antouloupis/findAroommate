from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .municipalities import MUNICIPALITIES
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile
import os, shutil, datetime
from django.conf import settings

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)  # e.g., city, municipality
    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='listings')
    current_year = datetime.date.today().year  # Get the current year
    title = models.CharField(max_length=25)
    description = models.TextField() #put a max length for description here
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='listings',default=1)#change default
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(15),MaxValueValidator(5000)]  # Set a maximum value if needed
    )
    size = models.PositiveIntegerField(validators=[MinValueValidator(15),MaxValueValidator(500)])
    date_listed = models.DateTimeField(auto_now_add=True) #save date on creation
    hidden = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    #Details
    bathrooms = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], null = True,blank=True)
    roommates = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)], null = True,blank=True)
    floor = models.SmallIntegerField(validators=[MaxValueValidator(15),MinValueValidator(-2)], null = True,blank=True)
    pet = models.BooleanField(default=False)
    #Extra details
    own_room = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    build_year = models.SmallIntegerField(null = True,blank=True,
    validators=[
        MaxValueValidator((current_year + 1)),
        MinValueValidator(1940)],
        )

    
    def __str__(self):
        return self.title

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_gallery')
    thumbnail = models.ImageField(upload_to='listing_gallery', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'image')  # Optional, ensures no duplicate images for a listing

    def save(self, *args, **kwargs):
        super(ListingImage, self).save(*args, **kwargs)  # Save the original image first to access the file path

        # Compress the image and save in the correct directory
        if self.image:
            img = Image.open(self.image)

            # Convert to RGB if necessary
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Define the target dimensions
            target_width = 1280
            target_aspect_ratio = 16 / 9
            target_height = int(target_width / target_aspect_ratio)

            # Resize the image to a fixed height and 16:9 aspect ratio
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

            # Compress image to WebP format
            output = BytesIO()
            img.save(output, format='WEBP', quality=70)
            output.seek(0)

            # Save compressed image in listing's folder
            compressed_image_name = str(self.listing.id) + "/" + f"{self.image.name.split('/')[-1].split('.')[0]}.webp"
            self.image.save(compressed_image_name, ContentFile(output.read()), save=False)

            # Create and save the thumbnail, ensuring the size is exactly 200x200
            img.thumbnail((200, 200))  # Resize image, keeping aspect ratio, so it fits within 200x200
            img = ImageOps.fit(img, (200, 200), Image.Resampling.LANCZOS)  # Crop to fit exactly 200x200

            thumb_output = BytesIO()
            img.save(thumb_output, format='WEBP', quality=90)
            thumb_output.seek(0)

            # Save the thumbnail in the thumbnails folder
            thumbnail_name = str(self.listing.id) + "/thumbnails/" + f"thumb_{self.image.name.split('/')[-1].split('.')[0]}.webp"
            self.thumbnail.save(thumbnail_name, ContentFile(thumb_output.read()), save=False)


        # Save the model again to update the compressed image and thumbnail paths
        super(ListingImage, self).save(*args, **kwargs)
        cleanup_uploads(os.path.join(settings.MEDIA_ROOT, 'listing_gallery'))

def cleanup_uploads(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  # Delete the file
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


