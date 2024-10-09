from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('saved/', views.savedPage, name="saved_listings"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.profile, name="profile"),
    path('update_password', views.change_password, name="update_password"),
]
