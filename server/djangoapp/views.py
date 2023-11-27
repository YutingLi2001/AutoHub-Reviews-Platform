from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CarModel
from .restapis import (
    get_dealers_from_cf,
    get_dealer_by_id_from_cf,
    get_dealer_reviews_from_cf,
    post_request
)
from datetime import datetime
import logging

# Configure logging for the application
logger = logging.getLogger(__name__)

DEALERSHIP_API_URL = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_dealerships"
REVIEW_API_URL = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/get_reviews"
POST_REVIEW_API_URL = "https://us-south.functions.appdomain.cloud/api/v1/web/ad39ee7e-0d06-4e9e-8de9-35be2c866619/dealership-package/post_review"

def render_static_page(request, page):
    """ Render a static page based on the provided page name. """
    return render(request, f'djangoapp/{page}.html')

def about(request):
    return render_static_page(request, 'about')

def contact(request):
    return render_static_page(request, 'contact')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid username or password.")
    return render_static_page(request, 'login')

def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

def registration_request(request):
    if request.method == 'POST':
        user = register_user(request)
        if user:
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("djangoapp:index")
    return render_static_page(request, 'registration')

def register_user(request):
    """ Register a new user if the POST data is valid. """
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')

    if password != password2:
        messages.error(request, "Passwords do not match.")
        return None
    
    if User.objects.filter(username=username).exists():
        messages.error(request, "Username already exists.")
        return None
    
    return User.objects.create_user(
        username=username, password=password,
        first_name=first_name, last_name=last_name
    )

def get_dealerships(request):
    """ Fetch and display list of all dealerships. """
    if request.method == "GET":
        dealerships = get_dealers_from_cf(DEALERSHIP_API_URL)
        return render(request, 'djangoapp/index.html', {"dealership_list": dealerships})
    return HttpResponse(status=405)

def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealer = get_dealer_by_id_from_cf(DEALERSHIP_API_URL, id=dealer_id)
        reviews = get_dealer_reviews_from_cf(REVIEW_API_URL, id=dealer_id)
        return render(request, 'djangoapp/dealer_details.html', {
            "dealer": dealer,
            "reviews": reviews
        })
    return HttpResponse(status=405)

def add_review(request, dealer_id):
    if request.method == 'POST' and request.user.is_authenticated:
        post_review(request, dealer_id)
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id)
    elif request.method == 'GET':
        return render_add_review_page(request, dealer_id)
    return HttpResponse(status=405)

def render_add_review_page(request, dealer_id):
    """ Render the add review page with the list of cars. """
    cars = CarModel.objects.all()
    return render(request, 'djangoapp/add_review.html', {
        "cars": cars,
        "dealer": get_dealer_by_id_from_cf(DEALERSHIP_API_URL, id=dealer_id)
    })

def post_review(request, dealer_id):
    """ Post a review to the dealership. """
    review_payload = create_review_payload(request, dealer_id)
    if review_payload:
        post_request(POST_REVIEW_API_URL, {"review": review_payload}, id=dealer_id)

def create_review_payload(request, dealer_id):
    """ Create the payload for posting a review based on the request. """
    user = request.user
    full_name = f"{user.first_name} {user.last_name}"
    car_id = request.POST.get("car")
    car = CarModel.objects.get(pk=car_id)
    payload = {
        "time": datetime.utcnow().isoformat(),
        "name": full_name,
        "dealership": dealer_id,
        "review": request.POST.get("content"),
        "purchase": "purchasecheck" in request.POST
    }
    if payload["purchase"]:
        payload.update({
            "purchase_date": request.POST.get("purchasedate"),
            "car_make": car.make.name,
            "car_model": car.name,
            "car_year": int(car.year)
        })
    return payload
