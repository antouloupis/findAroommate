from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from account.models import CustomUser
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def search_listings(request):
    listings = Listing.objects.filter(hidden=False)  # Start with all visible listings

    form_type = request.GET.get('form_type')

    if form_type == 'general_search':
        query = request.GET.get('search_query')
        if query:
            listings = listings.filter(
                Q(title__icontains=query) |
                Q(location__icontains=query) |
                Q(price__icontains=query)
            )
    elif form_type == 'filter':
        location = request.GET.get('location')
        price_min = request.GET.get('price-min')
        price_max = request.GET.get('price-max')

        if location:
            listings = listings.filter(location__icontains=location)

        if price_min:
            listings = listings.filter(price__gte=float(price_min))

        if price_max:
            listings = listings.filter(price__lte=float(price_max))


    return render(request, 'search/search_listings.html', {'listings': listings})

@login_required  # Ensure only authenticated users can access this view
@require_POST  # Only allow POST requests
def add_favorite(request, listing_id):
    
    user = request.user
    listing = get_object_or_404(Listing, id=listing_id)
    # Check if the listing is already in the user's favorites
    if listing in user.favorite_listings.all():
        return HttpResponse('<div>Already in favorites</div>')
    # Add the listing to the user's favorites
    user.favorite_listings.add(listing)
        
    return HttpResponse(request, '<div>hi</div>')