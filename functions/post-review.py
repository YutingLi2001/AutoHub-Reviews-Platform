import httpx
import random
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1

# Constants for configuration
API_KEY = ''  
SERVICE_URL = ''  
DATABASE_NAME = 'reviews'

# Configure the IAM authenticator and Cloudant client as global constants
authenticator = IAMAuthenticator(API_KEY)
cloudant_client = CloudantV1(authenticator=authenticator)
cloudant_client.set_service_url(SERVICE_URL)

async def add_review_to_database(review):
    """
    Adds a review to the Cloudant database, assigning it a random ID.

    :param review: The review data to add to the database.
    :return: A dictionary with status code and headers.
    """
    # Assign a random ID to the review document
    review['id'] = random.randint(15, 80)

    try:
        # Post the document to the Cloudant database
        await cloudant_client.post_document(db=DATABASE_NAME, document=review)
        # If successful, return a 201 Created status code
        return {
            'statusCode': 201,
            'headers': {'Content-Type': 'application/json'}
        }
    except httpx.HTTPStatusError as e:
        # If a HTTP error occurs, raise an exception with the status code and error message
        raise Exception(f'HTTP Error: {e.response.status_code} - {e.response.text}') from e
    except Exception as e:
        # If any other error occurs, raise an exception with the error message
        raise Exception(f'Error: {str(e)}') from e

async def main(params):
    """
    Main function that acts as an entry point for the script.

    :param params: Dictionary containing the parameters and review details.
    :return: The response from the add_review_to_database function.
    """
    # Extract the 'review' key from the params to get the review data
    review = params.get('json')
    if not review:
        raise ValueError('The "review" data is required.')

    # Call the function to add the review to the database
    return await add_review_to_database(review)