from django.contrib import admin
from .models import Listing
# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'municipality', 'price', 'date_listed', 'hidden')
    list_filter = ('hidden',)
    search_fields = ('title', 'municipality')
