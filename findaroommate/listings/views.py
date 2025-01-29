from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
from .models import Listing, ListingImage, Location
from account.models import Message
from django.http import HttpResponse


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

            # Validate the images before saving the listing
            images = request.FILES.getlist('image')  # Get the list of uploaded images

            # Check if the total number of images exceeds 10
            if len(images) > 10:
                error_message = "You can only upload a total of 10 images."
                return render(request, 'listings/create.html', {'form': form, 'error_message': error_message})

            # Initialize a list to hold error messages
            size_error_messages = []
            max_file_size = 5 * 1024 * 1024 

            # Validate image sizes
            for img in images:
                if img.size > max_file_size:
                    size_error_messages.append(f"{img.name} exceeds the maximum file size of 5 MB.")

           
            if size_error_messages:
                return render(request, 'listings/create.html', {
                    'form': form,
                    'error_message': size_error_messages
                })

            # Save the listing only after all validations are successful
            listing = form.save(commit=False)  
            listing.user = request.user        
            listing.location = location
            listing.save()

            # Save the images to the Listing
            for img in images:
                listing_image = ListingImage(listing=listing, image=img)
                listing_image.save()

            return redirect('front_page')
    else:
        form = ListingForm()
    return render(request, 'listings/create.html', {'form': form})

@login_required
def my_listings(request):
    user = request.user
    listings = Listing.objects.filter(user=user)
    context = {
        'listings': listings,
    }   
    return render(request, 'listings/my_listings.html',context)

def single_listing(request, id):
    listing = get_object_or_404(Listing,id=id)
    recipient = listing.user

    if not request.user.is_anonymous:
        existing_message = Message.objects.filter(
            sender=request.user,
            recipient=recipient,
            listing=listing,
            ).exists()
        if existing_message:
            return render(request,'listings/single.html',{'listing':listing,'sent':True})
        else:
            return render(request,'listings/single.html',{'listing':listing})
        
    else:
        return render(request,'listings/single.html',{'listing':listing, 'anon':True})
        
@login_required
def send_automated_message(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, id=listing_id)
        recipient = listing.user

        if request.user.is_authenticated:

            existing_message = Message.objects.filter(
                sender=request.user,
                recipient=recipient,
                listing=listing,
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

@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    if request.method == 'DELETE':
        listing.delete()
        html_message = '<div id="delete-message" class="alert alert-success alert-dismissible fade show mt-2 mb-auto" role="alert">Listing deleted!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
        return HttpResponse(html_message)
    else:
        return HttpResponse("Invalid request method", status=405)

@login_required
def edit_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, user=request.user)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        images_to_delete = request.POST.getlist('delete_images') 
        new_images = request.FILES.getlist('image')

        if form.is_valid():
            form.save()

            # Delete selected images
            if images_to_delete:
                ListingImage.objects.filter(id__in=images_to_delete, listing=listing).delete()

            # Add new images if any
            max_file_size = 5 * 1024 * 1024  # 5 MB
            size_error_messages = []
            if listing.images.count() + len(new_images) > 10:
                size_error_messages.append("You can only upload a total of 10 images.")
            for img in new_images:
                if img.size > max_file_size:
                    size_error_messages.append(f"{img.name} exceeds the maximum file size of 5 MB.")
                else:
                    listing_image = ListingImage(listing=listing, image=img)
                    listing_image.save()

            if size_error_messages:
                return render(request, 'listings/edit.html', {
                    'form': form,
                    'listing': listing,
                    'error_message': size_error_messages,
                })

            return redirect('front_page')

    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/edit.html', {
        'form': form,
        'listing': listing,
    })