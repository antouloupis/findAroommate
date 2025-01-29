from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_listings, name='search_listings'),
    path('filter/', views.filter_listings, name='filter_listings'),
    path('handle_favorite/<int:listing_id>/', views.handle_favorite, name='handle_favorite'),
    path('tenants/', views.filter_tenants, name='filter_tenants'),
]