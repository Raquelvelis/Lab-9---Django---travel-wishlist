# Admin configuration: makes Place editable in the Django admin site
from django.contrib import admin
from .models import Place

admin.site.register(Place)

