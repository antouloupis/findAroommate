from django.urls import path
from . import views

urlpatterns = [
path('<str:username>/',views.view_user,name="view_user")
]