from django.shortcuts import render
from search.forms import FilterForm  # Import the FilterForm from the search app


def front_page(request):
    filter_form = FilterForm(request.GET or None)  # Instantiate the form
    context = {
        'filter_form': filter_form,
    }    
    return render(request, 'core/index.html', context)