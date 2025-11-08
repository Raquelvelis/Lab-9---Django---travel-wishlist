# Views: functions that handle web requests and return responses
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm


def place_list(request):
    """Show list of places not visited and handle the "add place" form."""
    if request.method == 'POST':
        # Create a form filled with data the user submitted
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            # Save new Place to the database
            form.save()
            # Redirect to avoid re-posting the form if the user refreshes
            return redirect('place_list')
        else:
            # Form has errors; show them back to the user
            new_place_form = form
    else:
        # First visit to the page: show an empty form
        new_place_form = NewPlaceForm()
    
    # Get places not visited yet, sorted by name
    places = Place.objects.filter(visited=False).order_by('name')
    return render(request, 'travel_wishlist/wishlist.html', {
        'places': places,
        'new_place_form': new_place_form
    })


def places_visited(request):
    """Show list of places the user has marked as visited."""
    # Get places that are marked as visited, sorted by name
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


def place_was_visited(request, place_pk):
    """Mark a specific place as visited (only accepts POST)."""
    if request.method == 'POST':
        # Fetch the Place or return 404 if it doesn't exist
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    
    # Go back to the wishlist page
    return redirect('place_list')

