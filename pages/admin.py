from django.contrib import admin

from .models import Location

from mapbox_location_field.admin import MapAdmin

# Register your models here.

admin.site.register(Location, MapAdmin)

class LocationAdmin(admin.ModelAdmin):
    exclude = ('slug',)