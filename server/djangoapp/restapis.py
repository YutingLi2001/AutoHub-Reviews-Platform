import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features,SentimentOptions
import time

def get_request(url, **kwargs):
    # If argument contains API key
    api_key = kwargs.get("api_key")
    print("GET from {} ".format(url))
    try:
        if api_key:
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
        else:
            # Call get method of requests library with URL and parameters
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")

    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


def post_request(url, payload, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    print(payload)
    response = requests.post(url, params=kwargs, json=payload)
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


def get_dealers_from_cf(url, **kwargs):
    results = []
    state = kwargs.get("state")
    # Perform a GET request with or without the state parameter
    json_result = get_request(url, state=state) if state else get_request(url)

    if json_result:
        # Iterate over the returned dealers data
        for dealer in json_result:
            # Safely get the 'doc' key value
            dealer_doc = dealer.get("doc")
            if dealer_doc:
                # Proceed only if 'doc' is present
                try:
                    # Initialize a CarDealer object with values from 'doc'
                    dealer_obj = CarDealer(
                        address=dealer_doc.get("address", ""),
                        city=dealer_doc.get("city", ""),
                        full_name=dealer_doc.get("full_name", ""),
                        id=dealer_doc.get("id", 0),  # Assuming 'id' should be present, default to 0 if not found
                        lat=dealer_doc.get("lat", 0.0),
                        long=dealer_doc.get("long", 0.0),
                        st=dealer_doc.get("st", ""),
                        zip=dealer_doc.get("zip", "")
                    )
                    # Add the CarDealer object to the results list
                    results.append(dealer_obj)
                except KeyError as e:
                    # Handle specific missing key if necessary
                    print(f"Missing key in dealer data: {e}")
                except Exception as e:
                    # General exception catch, if needed (log or handle the unexpected error)
                    print(f"An error occurred: {e}")
            else:
                # Log or handle cases where 'doc' is not found
                print(f"'doc' key not found in dealer data: {dealer}")

    return results



def get_dealer_by_id_from_cf(url, id):
    json_result = get_request(url, id=id)

    if json_result:
        dealers = json_result[0]
        dealer_doc = dealers
        dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"],
                                id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"], full_name=dealer_doc["full_name"],
                                st=dealer_doc["st"], zip=dealer_doc["zip"])
    return dealer_obj


def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    id = kwargs.get("id")
    if id:
        json_result = get_request(url, id=id)
    else:
        json_result = get_request(url)
    if json_result:
        reviews = json_result["data"]["docs"]

        for dealer_review in reviews:
            review_obj = DealerReview(dealership=dealer_review["dealership"],
                                   name=dealer_review["name"],
                                   purchase=dealer_review["purchase"],
                                   review=dealer_review["review"])
            if "id" in dealer_review:
                review_obj.id = dealer_review["id"]
            if "purchase_date" in dealer_review:
                review_obj.purchase_date = dealer_review["purchase_date"]
            if "car_make" in dealer_review:
                review_obj.car_make = dealer_review["car_make"]
            if "car_model" in dealer_review:
                review_obj.car_model = dealer_review["car_model"]
            if "car_year" in dealer_review:
                review_obj.car_year = dealer_review["car_year"]
            
            sentiment = analyze_review_sentiments(review_obj.review)
            print(sentiment)
            review_obj.sentiment = sentiment
            results.append(review_obj)

    return results

def analyze_review_sentiments(text):
    # IBM Watson NLU service credentials
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/39e30a1e-daa0-43f9-baee-a2a9eab7d505"
    api_key = "lbhukj5iEH9QDmXoMTQWFJqlOs4X-i3_NPC9R_7XNsw2"
    
    # Setup the authenticator
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    
    # Set the service URL
    natural_language_understanding.set_service_url(url)
    
    # Analyze the sentiment
    try:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(sentiment=SentimentOptions(document=True))
        ).get_result()
        
        # Extract the sentiment label
        label = response['sentiment']['document']['label']
        return label
    
    except Exception as e:
        # Log the exception (or handle it as per your needs)
        print(f"Exception: {str(e)}")
        return None

