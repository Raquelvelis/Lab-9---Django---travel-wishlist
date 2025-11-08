# URL routes for the travel_wishlist app
# Each path connects a URL to a view function.
from django.urls import path
from . import views

urlpatterns = [
    # Home page: show wishlist and add new places
    path('', views.place_list, name='place_list'),
    # Page that lists places already visited
    path('visited', views.places_visited, name='places_visited'),
    # Button action to mark a place as visited
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'),
]
