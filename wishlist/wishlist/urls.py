# Project URL routes: sends the root URL traffic to our app
# Only change this if you add more apps or top-level routes.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin site
    path('admin/', admin.site.urls),
    # Send all other URLs to the travel_wishlist app
    path('', include('travel_wishlist.urls')),
]
