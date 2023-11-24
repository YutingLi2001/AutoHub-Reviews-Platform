from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    """
    Car Make represents a brand or manufacturer of cars.
    """
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return "Name: {}, Description: {}".format(self.name, self.description)

class CarModel(models.Model):
    """
    Car Model represents a specific model of car, which is made by a Car Make.
    """
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=50, choices=CAR_TYPES)
    year = models.DateField()

    def __str__(self):
        return "Name: {}, Dealer ID: {}, Type: {}, Year: {}".format(
            self.name, self.dealer_id, self.car_type, self.year.year)

# Consider converting these to Django models if they need to be stored in the database.
class CarDealer:
    """
    Car Dealer represents a car dealership, including its location and contact info.
    """
    # Initialization method with attributes defined
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Attributes with simple comments
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
        return "Dealer name: {}".format(self.full_name)

class DealerReview:
    """
    Dealer Review represents a customer's review of a car dealership.
    """
    # Initialization method with attributes defined
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment # Presumed to be provided by Watson NLU service
        self.id = id

    def __str__(self):
        return "Review: {}, Sentiment: {}".format(self.review, self.sentiment)