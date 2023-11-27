from django.db import models
from django.utils.timezone import now
import json

# Model for car make with relevant fields
class CarMake(models.Model):
    name = models.CharField(max_length=100, default='Make', null=False)
    description = models.CharField(max_length=500)

    # String representation for the CarMake
    def __str__(self):
        return f"Name: {self.name}"


# Model for car model with a relationship to CarMake and other specific fields
class CarModel(models.Model):
    # Constants for car types
    COUPE = 'Coupe'
    MINIVAN = 'Minivan'
    SEDAN = 'Sedan'
    SUV = 'SUV'
    TRUCK = 'Truck'
    WAGON = 'Wagon'
    
    # Choices tuple for car types
    CAR_TYPES = [
        (COUPE, 'Coupe'),
        (MINIVAN, 'Minivan'),
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (TRUCK, 'Truck'),
        (WAGON, 'Wagon'),
    ]

    # Foreign key relationship to CarMake
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=40, default='undefined', null=False)
    id = models.IntegerField(primary_key=True, default=1)  # Dealer id
    
    # Car type with choices
    type = models.CharField(
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN,
        null=False
    )
    
    # Year of the car model, defaulting to current year
    year = models.IntegerField(default=now().year)

    # String representation for the CarModel
    def __str__(self):
        return f"Name: {self.name}"


# Class representing a car dealer with various attributes
class CarDealer:

    def __init__(self, address, city, id, lat, long, st, zip, full_name):
        self.full_name = full_name
        self.address = address
        self.city = city
        self.id = id
        self.lat = lat
        self.long = long
        self.st = st
        self.zip = zip

    # String representation for the CarDealer
    def __str__(self):
        return f"Dealer Name: {self.full_name}"


# Class representing a dealer review with both required and optional attributes
class DealerReview:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes initialized as empty strings
        self.purchase_date = ""
        self.purchase_make = ""
        self.purchase_model = ""
        self.purchase_year = ""
        self.sentiment = ""
        self.id = ""

    # String representation for the DealerReview
    def __str__(self):
        return f"Review: {self.review}"

    # Converts the object to JSON
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# Class for posting a review, similar to DealerReview, but with different fields for the car
class ReviewPost:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""

    # Converts the object to JSON
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
