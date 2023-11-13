import requests

YELP_API_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
API_KEY = "U6p8By2lF8kJHiFepNifD016NGlFtI1QGWyWPd-jxoOhAkZxdD6cW0JPRFg3yeJrqkRfK2pFbkcAr1jcUAqcaNIeuL3aDiNfaxrDwglp0CwufZxrmRikZCgKlu41ZXYx"


def search_businesses(term, location):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    params = {
        "term": term,
        "location": location,
    }

    response = requests.get(YELP_API_ENDPOINT, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
