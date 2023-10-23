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


# REPORT 1
# Name                              Stmts   Miss  Cover
# -----------------------------------------------------
# homepage/__init__.py                  0      0   100%
# homepage/admin.py                     1      0   100%
# homepage/apps.py                      4      0   100%
# homepage/migrations/__init__.py       0      0   100%
# homepage/models.py                    1      0   100%
# homepage/tests.py                    15      0   100%
# homepage/urls.py                      3      0   100%
# homepage/views.py                     4      1    75%
# homepage/yelp_api.py                 10      1    90%
# manage.py                            12      2    83%
# travel_itinerary/__init__.py          0      0   100%
# travel_itinerary/settings.py         18      0   100%
# travel_itinerary/urls.py              4      0   100%
# yelp_api.py                          10      6    40%
# -----------------------------------------------------
# TOTAL                                82     10    88%

# REPORT 2
# Name                              Stmts   Miss  Cover
# -----------------------------------------------------
# homepage/__init__.py                  0      0   100%
# homepage/admin.py                     1      0   100%
# homepage/apps.py                      4      0   100%
# homepage/migrations/__init__.py       0      0   100%
# homepage/models.py                    1      0   100%
# homepage/tests.py                    33      0   100%
# homepage/urls.py                      3      0   100%
# homepage/views.py                     4      1    75%
# homepage/yelp_api.py                 10      0   100%
# manage.py                            12      2    83%
# travel_itinerary/__init__.py          0      0   100%
# travel_itinerary/settings.py         18      0   100%
# travel_itinerary/urls.py              4      0   100%
# yelp_api.py                          10      6    40%
# -----------------------------------------------------
# TOTAL                               100      9    91%
