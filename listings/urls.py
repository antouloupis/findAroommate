from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_listing, name="create_listing"),
    path('my-listings/', views.my_listings, name="my_listings"),
    path('<int:id>/', views.single_listing, name="single"),
    path('send_message/<int:listing_id>/', views.send_automated_message, name='send_automated_message'),
]