from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarModel
from .models import CarMake
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Render the about page
def about(request):
    """Render a static about page."""
    return render(request, 'djangoapp/about.html')

# Render the contact page
def contact(request):
    """Return a static contact page."""
    return render(request, 'djangoapp/contact.html')

# Handle sign in request
def login_request(request):
    """Process the sign in request."""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # Using `messages` to pass errors to templates
            messages.error(request, "Invalid username or password.")
    # GET and other methods will fall to this return statement
    return render(request, 'djangoapp/login.html')

# Handle sign out request
def logout_request(request):
    """Process the sign out request."""
    logout(request)
    return redirect('djangoapp:index')

# Handle sign up request
def registration_request(request):
    """Process the sign up request."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        # Check if user exists using Django's built-in method
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            # Log the user in and redirect to index page
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('djangoapp:index')
        else:
            messages.error(request, "User already exists.")
    # GET and other methods will fall to this return statement
    return render(request, 'djangoapp/registration.html')

# Render the index page with a list of dealerships
def get_dealerships(request):
    """Render the index page with a list of dealerships."""
    # Add code to fetch dealerships and pass to the context
    # context['dealerships'] = fetch_dealerships()
    return render(request, 'djangoapp/index.html')


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

