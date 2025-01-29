from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),  
    path('search/', include('search.urls')),  
    path('account/', include('account.urls')),  
    path('listings/', include('listings.urls')), 
    path('users/',include('profiles.urls')),
    
]
admin.site.site_header = "FindAroommate Admin"
admin.site.site_title = "FindAroommate Admin Portal"
admin.site.index_title = "Welcome to FindAroommate"