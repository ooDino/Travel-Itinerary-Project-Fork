from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, Mock
from homepage.yelp_api import search_businesses, YELP_API_ENDPOINT
from homepage import yelp_api
from requests.exceptions import HTTPError
from homepage.models import Business
from homepage.views import search_results

# Create your tests here.


class YelpApiTest(TestCase):
    @patch("yelp_api.requests.get")
    def test_search_businesses(self, mock_get):
        mock_data = {
            "businesses": [
                {
                    "name": "Sample Restaurant",
                    # ... add more fields here - this is just to test something simple for now
                }
            ]
        }
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        result = search_businesses("restaurants", "San Francisco")

        self.assertEqual(result["businesses"][0]["name"], "Sample Restaurant")

    ################################ WHAT WAS RUN ON REPORT 1 ^^^^^^^^^^
    ################################ ADDED AFTER REPORT 1 AND TESTED WITH REPORT 2 VVVVV
    @patch("yelp_api.requests.get")
    def test_search_businesses_expected_behavior(self, mock_get):
        mock_data = {
            "businesses": [
                {
                    "name": "Sample Cafe",
                    # ... add more fields here - this is just to test something simple for now
                }
            ]
        }
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        result = search_businesses("cafe", "Los Angeles")

        self.assertEqual(result["businesses"][0]["name"], "Sample Cafe")

    @patch("yelp_api.requests.get")
    def test_search_businesses_error_handling(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404  # Not Found error for demonstration
        mock_response.json.return_value = {"error": "Not Found"}
        mock_response.raise_for_status.side_effect = HTTPError("Not Found")
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError):
            search_businesses("invalid_term", "invalid_location")


#########################################


# Integration testing
class SearchResultsIntegrationTest(TestCase):
    def test_search_results_successful(self):
        # test simulates a successful interaction between the search_results view and the Yelp API.
        response = self.client.get(
            reverse("search_results"), {"term": "hotel", "location": "New Jersey"}
        )

        # check if status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # check if some expected content is in the response
        self.assertContains(response, "Riviera Hotel")  # some random value that exists

    def test_search_results_error(self):
        # test simulates an error condition, i.e. providing an invalid location
        response = self.client.get(
            reverse("search_results"),
            {"term": "restaurant", "location": "invalid_location"},
        )

        # confirm if status code is 200 OK (bc view handles errors gracefully)
        self.assertEqual(response.status_code, 200)

        # confirm if the error message is displayed
        self.assertContains(
            response, "Sorry, there was an error processing your request."
        )


#### RESULTS OF INTEGRATION TEST
# (.travel_itinerary_venv) cristianstatescu@Cristians-MacBook-Pro CSc456 % python manage.py test homepage
#
# Found 5 test(s).
# Creating test database for alias 'default'...
# System check identified no issues (0 silenced).
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.641s
#
# OK
# Destroying test database for alias 'default'...
