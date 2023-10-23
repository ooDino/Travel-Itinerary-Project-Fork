from django.test import TestCase
from unittest.mock import patch, Mock
from homepage.yelp_api import search_businesses
from homepage import yelp_api
from requests.exceptions import HTTPError

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
