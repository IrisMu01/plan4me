from django.contrib import admin
from .models import Poi, PoiType, Event, Location, SearchReq

# Register your models here.

@admin.register(SearchReq)
class SearchReqAdmin(admin.ModelAdmin):
    list_display = ('city', 'date_from', 'date_to', 'min_budget', 'max_budget', 'keywords')
    fields = ['city', ('date_from', 'date_to'), ('min_budget', 'max_budget'), 'keywords']

# register the admin class with the associated model
@admin.register(Poi)
# defining the admin class
class PoiAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'location', 'priceLV', 'rating')
    list_filter = ('location', 'priceLV')

# alternative way to register
@admin.register(PoiType)
class PoiTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'starting_time')

class LocationAdmin(admin.ModelAdmin):
    list_dispaly = ('city', 'country')
admin.site.register(Location, LocationAdmin)