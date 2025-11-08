# Data model for the app
# Each Place is a row in the database with a name and a visited flag.
from django.db import models

class Place(models.Model):
    # Name of the place the user wants to visit
    name = models.CharField(max_length=200)
    # Has the user visited this place yet?
    visited = models.BooleanField(default=False)
    
    def __str__(self):
        # How this object shows up in admin and Django shell
        return self.name

