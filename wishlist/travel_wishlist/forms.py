# Forms turn user input into Python objects we can save
from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    """Simple form to create a new Place with just a name."""
    class Meta:
        model = Place
        fields = ('name', )
