from django.shortcuts import render, redirect
from .forms import ListingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
# return to a page after valid form is submitted
            return redirect('front_page')
    else:
        form = ListingForm()
    return render(request, 'listings/create.html', {'form': form})
