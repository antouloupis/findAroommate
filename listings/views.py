from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
from .models import Listing, ListingImage, Location
from account.models import Message
from django.http import HttpResponse

# Create your views here.
@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)


        if form.is_valid():
            location_name = request.POST.get('location')  
          
            # Get or create the Location object
            location, created = Location.objects.get_or_create(
                name=location_name,
            )

            listing = form.save(commit=False)  # Don't save to the database yet
            listing.user = request.user        # Set the listing user to the current user
            listing.location = location
            listing.save()
            images = request.FILES.getlist('image')  # Get the list of uploaded images

            # Check if the total number of images exceeds 10
            if listing.images.count() + len(images) > 10:
                error_message = "You can only upload a total of 10 images."
                return render(request, 'listings/create.html', {'form': form, 'error_message': error_message})

            # Initialize a list to hold error messages
            size_error_messages = []
            max_file_size = 3 * 1024 * 1024  # 3 MB in bytes

            # Validate image sizes
            for img in images:
                if img.size > max_file_size:
                    size_error_messages.append(f"{img.name} exceeds the maximum file size of 3 MB.")

            # If any image is too large, return an error
            if size_error_messages:
                return render(request, 'listings/create.html', {
                    'form': form,
                    'error_message': size_error_messages
                })
            else:
            # Save the images to the Listing
                for img in images:
                    listing_image = ListingImage(listing=listing, image=img)
                    listing_image.save()  # This will trigger any save methods (like compression)

                # return to a page after valid form is submitted
                return redirect('front_page')
    else:
        form = ListingForm()
    return render(request, 'listings/create.html', {'form': form})

def my_listings(request):
    user = request.user
    listings = Listing.objects.filter(user=user)
    context = {
        'listings': listings,
    }   
    return render(request, 'listings/my_listings.html',context)\

def single_listing(request, id):
    listing = get_object_or_404(Listing,id=id)
    recipient = listing.user

    if not request.user.is_anonymous:
        existing_message = Message.objects.filter(
            sender=request.user,
            recipient=recipient,
            listing=listing,
            ).exists()

        return render(request,'listings/single.html',{'listing':listing,'sent':True})
        
    else:
        return render(request,'listings/single.html',{'listing':listing, 'anon':True})
        
    return render(request,'listings/single.html',{'listing':listing})

    


@login_required
def send_automated_message(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, id=listing_id)
        recipient = listing.user

        if request.user.is_authenticated:

            existing_message = Message.objects.filter(
                sender=request.user,
                recipient=recipient,
                listing=listing,  # Assuming you are using a ForeignKey to Listing in Message
            ).exists()

            if existing_message:
                return HttpResponse("You have already sent a message for this listing.")

            Message.objects.create(
                listing=listing,
                content="Hello, I am intrested in this listing. Let's get in touch!",
                sender=request.user,
                recipient=recipient,
            )

            return HttpResponse("Message sent!")
        else:
            return HttpResponse("You must be logged in to send a message.", status=403)
    else:
        return HttpResponse("Invalid request method.", status=405)


