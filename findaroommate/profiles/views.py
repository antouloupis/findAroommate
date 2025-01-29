from django.shortcuts import render, get_object_or_404
from account.models import CustomUser
from .models import Profile

def view_user(request, username):
    user = get_object_or_404(CustomUser,username=username)
    profile = get_object_or_404(Profile, user=user)
    if profile.hidden:
        return render(request,'profiles/profile_hidden.html')
    else:
        return render(request,'profiles/profile.html',{'profile': profile})


