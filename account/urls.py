from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('saved/', views.savedPage, name="saved_listings"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.profile, name="edit_profile"),
    path('change-details/', views.change_details, name="change_details"),
    path('change-password/', views.change_password, name="change_password"),
    path('activate-user/<uidb64>/<token>', views.activate_user, name="activate"),
    path('my-listings/',views.my_listings_tab,name="my_listings_tab"),
    path('inbox/', views.inbox, name='inbox'),
]
