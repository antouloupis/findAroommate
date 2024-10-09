from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from account.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required


#Create views here
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'account/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('front_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('front_page')
            else:
                messages.info(request, 'Username or password is wrong')
        return render(request, 'account/login.html')

@login_required
def savedPage(request):
    return render(request, 'account/saved.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'POST':
        # Get the current user
        user = request.user
        # Initialize a variable to track whether any changes were made
        changes_made = False
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')

        # Check if the username or email has changed
        if new_username and new_username != user.username:
            if CustomUser.objects.filter(username=new_username).exists():
                messages.error(request, 'Username is taken')
            else:
                user.username = new_username
                changes_made = True  # Indicate that a change was made

        if new_email and new_email != user.email:
            if CustomUser.objects.filter(email=new_email).exists():
                messages.error(request, 'Email is already being used')
            else:
                user.email = new_email
                changes_made = True  # Indicate that a change was made
        

        # Save changes if there were no errors
        if changes_made:
            try:
                # Validate the user instance
                user.full_clean()  # This will call the clean method
                user.save()  # Save the user only if validation passes

                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)  # Add each validation error to messages
                return redirect('profile')
    
    # For GET requests, render the profile template with the current user's information
    return render(request, 'account/profile.html')
    

#The page for requesting to change a password
def change_password(request):
    
    
    if request.method == 'POST':
        user = request.user
        old_pw= request.POST.get('old-pw')
        new_pw = request.POST.get('new-pw')
        new_pw2 = request.POST.get('new-pw2')

        if user.check_password(old_pw): #if password matches
            if new_pw == new_pw2:
                user.password = new_pw
                try:
                    # Validate the new password
                    validate_password(new_pw, user)
                    user.set_password(new_pw)
                    user.save()  # Save the user only if validation passes
                    messages.success(request, 'Password updated successfully.')
                    logout(request)
                    return redirect('login')
                except ValidationError as e:
                    for error in e.messages:
                        messages.error(request, error)  # Add each validation error to messages
            else:
                messages.error(request, 'The new passwords do not match.')
        else:
            messages.error(request, 'The current password is incorrect.')
    
    return render(request, 'account/change_password.html')
