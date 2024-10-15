from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from account.models import CustomUser
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FilterForm
from django.db.models import Q


def search_listings(request):
    listings = Listing.objects.filter(hidden=False)  # Start with all visible listings
    query = request.GET.get('query','')
    filters = FilterForm(request.GET or None)
    
    if query:
        listings = listings.filter(
        Q(title__icontains=query) | 
        Q(municipality__icontains=query) | 
        Q(description__icontains=query)
        )
    
    
    # If filter form is submitted, apply additional filters
    if filters.is_valid():
        municipality = filters.cleaned_data.get('municipality')
        own_room = filters.cleaned_data.get('own_room')
        garden = filters.cleaned_data.get('garden')
        parking = filters.cleaned_data.get('parking')
        elevator = filters.cleaned_data.get('elevator')
        smoking = filters.cleaned_data.get('smoking')
        roommates_min = filters.cleaned_data.get('roommates_min')
        roommates_max = filters.cleaned_data.get('roommates_max')
        floor_min = filters.cleaned_data.get('floor_min')
        floor_max = filters.cleaned_data.get('floor_max')
        bathrooms_min = filters.cleaned_data.get('bathrooms_min')
        bathrooms_max = filters.cleaned_data.get('bathrooms_max')
        price_min = filters.cleaned_data.get('price_min')
        price_max = filters.cleaned_data.get('price_max')
        size_min = filters.cleaned_data.get('size_min')
        size_max = filters.cleaned_data.get('size_max')

        if own_room:
            listings = listings.filter(own_room=own_room)
        if garden:
            listings = listings.filter(garden=garden)
        if parking:
            listings = listings.filter(parking=parking)
        if elevator:
            listings = listings.filter(elevator=elevator)
        if smoking:
            listings = listings.filter(smoking=smoking)
        if municipality:
            listings = listings.filter(municipality=municipality)
        if price_min:
            listings = listings.filter(price__gte=price_min)
        if price_max:
           listings = listings.filter(price__lte=price_max)
        if bathrooms_min:
            listings = listings.filter(bathrooms__gte=bathrooms_min)
        if bathrooms_max:
            listings = listings.filter(bathrooms__lte=bathrooms_max)
        if floor_min:
            listings = listings.filter(floor__gte=floor_min)
        if floor_max:
            listings = listings.filter(floor__lte=floor_max)
        if roommates_min:
            listings = listings.filter(roommates__gte=roommates_min)
        if roommates_max:
            listings = listings.filter(roommates__lte=roommates_max)

    context = {
        'query': query,
        'FilterForm': filters,
        'listings': listings,
    }
    
    return render(request, 'search/search_listings.html', context)

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
        
    return HttpResponse('<button class="btn btn-danger"> Saved in favorites </button>')