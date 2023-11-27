from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarModel, CarMake, CarDealer, DealerReview, ReviewPost
from .restapis import get_request, post_request, get_dealers_from_cf, get_dealer_by_id_from_cf, get_dealer_reviews_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# About view to render static about page
def about(request):
    return render(request, 'djangoapp/about.html')

# Contact view to render static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')

# View to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

# View to handle sign out request
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# View to handle sign up request
def registration_request(request):
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html')

    if request.method == 'POST':
        # Retrieving form data
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']  # Confirm password field
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        # Check if passwords match
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'djangoapp/registration.html')

        # Check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'djangoapp/registration.html')

        # Creating a new user
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect("djangoapp:index")
        except Exception as e:
            logger.error(f"Error creating a new user: {e}")
            messages.error(request, "An error occurred during registration.")
            return render(request, 'djangoapp/registration.html')

# View to render list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        context = {}
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_dealerships"
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
        return render(request, 'djangoapp/index.html', context)

# View to render dealer details (reviews)
def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_dealerships"
        dealer = get_dealer_by_id_from_cf(dealer_url, id=id)
        context["dealer"] = dealer
                      
        review_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_reviews"
        reviews = get_dealer_reviews_from_cf(review_url, id=id)
        print(reviews)
        context["reviews"] = reviews
        
        return render(request, 'djangoapp/dealer_details.html', context)

# View to post a review
def add_review(request, id):
    context = {}
    dealer_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_dealerships"
    dealer = get_dealer_by_id_from_cf(dealer_url, id=id)
    context["dealer"] = dealer
    if request.method == 'GET':
        cars = CarModel.objects.all()
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            first_name = user.first_name
            last_name = user.last_name
            full_name = f"{first_name} {last_name}"
            print(request.POST)
            payload = dict()
            car_id = request.POST["car"]
            car = CarModel.objects.get(pk=car_id)

            payload["time"] = datetime.utcnow().isoformat()
            payload["name"] = full_name
            payload["dealership"] = id
            payload["id"] = id
            payload["review"] = request.POST["content"]
            
            # Check if "purchasecheck" is checked
            if "purchasecheck" in request.POST and request.POST["purchasecheck"] == 'on':
                payload["purchase"] = True
                payload["purchase_date"] = request.POST["purchasedate"]
                payload["car_make"] = car.make.name
                payload["car_model"] = car.name
                payload["car_year"] = int(car.year)
            else:
                payload["purchase"] = False
            
            json_payload = {}
            json_payload["review"] = payload
            review_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/post_review"
            post_request(review_url, json_payload, id=id)
        return redirect("djangoapp:dealer_details", id=id)