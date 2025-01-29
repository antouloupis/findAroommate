from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm
from .models import CustomUser, Message
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from listings.models import Listing
from profiles.models import Profile
from profiles.forms import ProfileForm



User = get_user_model()

def deny_if_login(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('front_page') 
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def send_activation_email(user,request):
    current_site= get_current_site(request)
    subject = 'Activate your account'
    body = render_to_string('account/activate.html',{
        'user':user,
        'domain':current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=subject,body=body,from_email=settings.EMAIL_FROM_USER,
    to=[user.email]
    )

    email.send()

@deny_if_login
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            
            # Create and save the corresponding Profile instance
            Profile.objects.create(user=user, email=user.email)

            send_activation_email(user, request)
            messages.info(request, 'Please verify your email address before logging in.')
            return redirect('login')
    context = {'form':form}
    return render(request, 'account/register.html', context)


def loginPage(request):
    # Redirect already authenticated users
    if request.user.is_authenticated:
        return redirect('front_page') 

    # Initialize the form
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser or user.is_email_verified:
                    login(request, user)
                    next_url = request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    return redirect('front_page')
                else:
                    messages.info(request, 'Please verify your email address before logging in.')
            else:
                messages.info(request, 'Username or password is incorrect.')

    return render(request, 'account/login.html', {'form': form})

@login_required
def savedPage(request):
    user = request.user
    listings = user.favorite_listings.all()
    return render(request, 'account/saved.html',{'listings':listings})

@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('login')

@login_required
def profile(request):

    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved')
            return redirect('edit_profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
    
@login_required
def change_password(request):
    
    if request.method == 'POST':
        user = request.user
        old_pw= request.POST.get('old-pw')
        new_pw = request.POST.get('new-pw')
        new_pw2 = request.POST.get('new-pw2')

        if user.check_password(old_pw): #If password matches
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
    
    return render(request, 'account/tabs/change_password.html')

def activate_user(request, uidb64, token):
    try:
        # Decode uidb64 to get the user id
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (ObjectDoesNotExist, TypeError, ValueError, OverflowError):
        user = None

    # Check if the user and token are valid
    if user is not None and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Email verified successfully.')
        return redirect('login')  # Redirect to the login page
    
    # If the user is None or the token is invalid, redirect to login with an error message
    messages.add_message(request, messages.ERROR, 'Invalid activation link.')
    return redirect('login')  


@login_required
def change_details(request):
    if request.method == 'POST':
        # Get the current user
        user = request.user
        # Initialize a variable to track whether any changes were made
        changes_made = False
        new_email = request.POST.get('email')

        # Check if the username or email has changed
        if new_email and new_email != user.email:
            if CustomUser.objects.filter(email=new_email).exists():
                messages.error(request, 'Email is already being used')
            else:
                user.email = new_email
                changes_made = True
        

        if changes_made:
            try:
                
                user.full_clean()
                user.save()  # Save the user only if validation passes

                messages.success(request, 'Profile updated successfully.')
                return redirect('change_details')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)  # Add each validation error to messages
                return redirect('change_details')
    
    # For GET requests, render the profile template with the current user's information
    return render(request, 'account/tabs/change_details.html')

@login_required
def my_listings_tab(request):

    user = request.user
    listings = Listing.objects.filter(user=user)
    context = {
        'listings': listings,
    }   
    return render(request, 'account/tabs/my_listings_tab.html',context)

@login_required
def inbox(request):
    user = request.user
    inbox = Message.objects.filter(recipient=user,recipient_deleted=False).order_by('-date')
    return render(request,'account/tabs/inbox.html',{'inbox':inbox})

