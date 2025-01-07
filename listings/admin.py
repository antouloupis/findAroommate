from django.contrib import admin
from .models import Listing, ListingImage, Location
# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'price', 'date_listed', 'hidden')
    list_filter = ('hidden',)
    search_fields = ('title',)


admin.site.register(ListingImage)

admin.site.register(Location)

