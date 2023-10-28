import requests

#client ID = "Ux-ogoVyLcFKsVukvbTb3A"
YELP_API_ENDPOINT = " https://api.yelp.com/v3/businesses/search"
API_KEY = "U6p8By2lF8kJHiFepNifD016NGlFtI1QGWyWPd-jxoOhAkZxdD6cW0JPRFg3yeJrqkRfK2pFbkcAr1jcUAqcaNIeuL3aDiNfaxrDwglp0CwufZxrmRikZCgKlu41ZXYx"

def search_business(location, term):
    headers = {"authorization": f"bearer {API_KEY}"}

    params = {
        "location" : location,
        "term" : term,
    }

    response = requests.get(YELP_API_ENDPOINT, headers=headers, params = params)

    if( response.status_code == 200):
        return response.json()
    else:
        response.raise_for_status()


## travel_itineray. manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_itinerary.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
    
