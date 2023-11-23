import httpx
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1

# Constants (replace with your actual values)
API_KEY = ''
SERVICE_URL = ''
DATABASE_NAME = 'reviews'

# Configure the IAM authenticator and Cloudant client as global constants
AUTHENTICATOR = IAMAuthenticator(API_KEY)
CLIENT = CloudantV1(authenticator=AUTHENTICATOR)
CLIENT.set_service_url(SERVICE_URL)

async def get_dealer_reviews(dealer_id):
    """
    Retrieves reviews from a Cloudant database based on the dealer ID.
    
    :param dealer_id: The ID of the dealer for which to retrieve reviews.
    :return: A dictionary with status code, headers, and body of the response.
    """
    try:
        response = await CLIENT.post_find(
            db=DATABASE_NAME,
            selector={'dealership': dealer_id}
        )
        docs = response.get_result().get('docs', [])
        return {
            'statusCode': 200 if docs else 404,
            'headers': {'Content-Type': 'application/json'},
            'body': docs
        }
    except ApiException as e:
        return {
            'statusCode': e.code,
            'body': {'error': e.message}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }

async def main(params):
    """
    Main function to handle the API call.
    
    :param params: Dictionary containing the parameters for the function.
    :return: The result from the get_dealer_reviews function.
    """
    dealer_id = params.get('dealerId')
    if not dealer_id:
        return {'statusCode': 400, 'body': {'error': 'Dealer ID is required'}}
    
    try:
        dealer_id = int(dealer_id)
    except ValueError:
        return {'statusCode': 400, 'body': {'error': 'Invalid Dealer ID format'}}

    return await get_dealer_reviews(dealer_id)
