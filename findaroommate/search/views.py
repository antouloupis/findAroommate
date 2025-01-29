from django.shortcuts import render, get_object_or_404, reverse
from listings.models import Listing
from account.models import CustomUser
from profiles.models import Profile
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FilterForm, FilterUsersForm
from django.db.models import Q
from django.middleware.csrf import get_token
from django.urls import reverse


def search_listings(request):
    filter_form = FilterForm(request.GET or None) 
    listings = Listing.objects.filter(hidden=False)  # Start with all visible listings
    search_query = request.GET.get('query', '')

    if search_query:
        query = (
            Q(title__icontains=search_query) |
            Q(location__name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(address__icontains=search_query)
        )
        listings = listings.filter(query)

    context = {
        'query': search_query,
        'listings': listings,
        'filter_form': filter_form, 
    }

    return render(request, 'search/search_listings.html', context)

def filter_listings(request):
    listings = Listing.objects.filter(hidden=False)  
    filters = FilterForm(request.GET or None)

    if filters.is_valid():
        query = Q()

        area = filters.cleaned_data.get('area')
        own_room = filters.cleaned_data.get('own_room')
        garden = filters.cleaned_data.get('garden')
        parking = filters.cleaned_data.get('parking')
        elevator = filters.cleaned_data.get('elevator')
        smoking = filters.cleaned_data.get('smoking')
        pet = filters.cleaned_data.get('pet')
        price_min = filters.cleaned_data.get('price_min')
        price_max = filters.cleaned_data.get('price_max')
        bathrooms_min = filters.cleaned_data.get('bathrooms_min')
        size_min = filters.cleaned_data.get('size_min')
        roommates_max = filters.cleaned_data.get('roommates_max')
        floor_min = filters.cleaned_data.get('floor_min')
        floor_max = filters.cleaned_data.get('floor_max')

        if area:
            query &= Q(location__name=area)
        if own_room != '':
            query &= Q(own_room=own_room == 'True')
        if garden != '':
            query &= Q(garden=garden == 'True')
        if parking != '':
            query &= Q(parking=parking == 'True')
        if elevator != '':
            query &= Q(elevator=elevator == 'True')
        if smoking != '':
            query &= Q(smoking=smoking == 'True')
        if pet != '':
            query &= Q(pet=pet == 'True')
        if price_min is not None:
            query &= Q(price__gte=price_min)
        if price_max is not None:
            query &= Q(price__lte=price_max)
        if bathrooms_min is not None:
            query &= Q(bathrooms__lte=bathrooms_min)
        if size_min is not None:
            query &= Q(size__gte=size_min)
        if roommates_max is not None:
            query &= Q(roommates__lte=roommates_max)
        if floor_min is not None:
            query &= Q(floor__gte=floor_min)
        if floor_max is not None:
            query &= Q(floor__lte=floor_max)

        listings = listings.filter(query)

    context = {
        'listings': listings,
        'filter_form': filters, 
    }

    return render(request, 'search/search_listings.html', context)

@require_POST 
def handle_favorite(request, listing_id):

    user = request.user
    # Check if the user is authenticated
    if user.is_anonymous:
        if request.headers.get('HX-Request'):
            # For HTMX requests, send a response that triggers a redirect
            response = HttpResponse(status=403)
            response['HX-Redirect'] = reverse('login')
            return response

    csrf_token = get_token(request)
    
    listing = get_object_or_404(Listing, id=listing_id)

    post_url = reverse('handle_favorite', args=[listing_id])

    # Check if the listing is already in the user's favorites
    if listing in user.favorite_listings.all():
        user.favorite_listings.remove(listing)
        htmx = f"""<button class="btn btn-outline-danger" hx-headers='{{"X-CSRFToken": "{csrf_token}"}}' 
                    hx-post="{post_url}" hx-swap="outerHTML">
                        Add to favorites
                    </button>"""
        return HttpResponse(htmx)
    # Add the listing to the user's favorites
    user.favorite_listings.add(listing)
    htmx = f"""
    <button class="btn btn-danger" hx-headers='{{"X-CSRFToken": "{csrf_token}"}}' hx-post="{post_url}" hx-swap="outerHTML">
        Saved
    </button>
    """   
    return HttpResponse(htmx)

def filter_tenants(request):
    profiles = Profile.objects.filter(hidden=False)
    filters = FilterUsersForm(request.GET or None)

    if filters.is_valid():
        area = filters.cleaned_data.get('area')
        pet = filters.cleaned_data.get('pet')

        if area:
            profiles = profiles.filter(location=area.location)
        if pet == 'True':
            profiles = profiles.filter(pets='True')
        elif pet =='False':
            profiles = profiles.filter(pets='False')
        
    
    context = {
        'profiles': profiles,
        'tenant_form': filters, 
    }

    return render(request, 'search/search_tenants.html', context)

