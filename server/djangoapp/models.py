from django.db import models
from django.utils.timezone import now

# Using Python's enum library to define choices in a more robust way
from enum import Enum

class CarType(Enum):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'

    @classmethod
    def choices(cls):
        # This method will turn the enum into a tuple list ready for Django's choices
        return [(key.value, key.name.title()) for key in cls]

# Each model class will have a docstring explaining the purpose of the model
class CarMake(models.Model):
    """
    Car Make represents the brand of the car.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)  # Use TextField for long strings

    def __str__(self):
        # Improved readability using f-strings
        return f"Name: {self.name}, Description: {self.description}"

class CarModel(models.Model):
    """
    Car Model represents a specific model of a car which belongs to a car make.
    """
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()  # Assuming this refers to an external ID
    car_type = models.CharField(
        max_length=50,
        choices=CarType.choices(),  # Using the choices method from the CarType enum
    )
    year = models.DateField()

    def __str__(self):
        # Using f-strings and accessing the year directly from the date object
        return f"Name: {self.name}, Dealer ID: {self.dealer_id}, Type: {self.car_type}, Year: {self.year.year}"

# The following classes are not Django models, but if they should be, they need to inherit from models.Model
class CarDealer:
    """
    Car Dealer represents the information of a car dealership.
    """
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Using descriptive parameter names and adding comments where necessary
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return f"Dealer name: {self.full_name}"

class DealerReview:
    """
    Dealer Review contains customer reviews for a dealership, including sentiment analysis.
    """
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment  # Presumed to be calculated via Watson NLU service
        self.id = id

    def __str__(self):
        return f"Review: {self.review}, Sentiment: {self.sentiment}"