from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_listings, name='search_listings'),
    path('add_favorite/<int:listing_id>/', views.add_favorite, name='add_favorite'),
]