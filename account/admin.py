from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Message

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add this to the CustomUserAdmin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('favorite_listings',)}),  # Add favorite_listings field
    )

    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')

    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
