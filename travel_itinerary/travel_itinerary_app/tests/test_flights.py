from django.test import TestCase
from unittest.mock import patch
from travel_itinerary_app.flights import Flight, airport_id_locator, flights_finder


class FlightTestCase(TestCase):

    def test_flight_initialization(self):
        # Test initialization of the Flight class
        flight = Flight("JFK", "LAX", "$500", "2023-12-01", "2023-12-05", "Delta")
        self.assertEqual(flight.from_airport, "JFK")
        self.assertEqual(flight.to_airport, "LAX")
        self.assertEqual(flight.cost, "$500")
        self.assertEqual(flight.dates_departure, "2023-12-01")
        self.assertEqual(flight.dates_arrival, "2023-12-05")
        self.assertEqual(flight.airlines_name, "Delta")

    def test_flight_str(self):
        # Test string representation of the Flight class
        flight = Flight("JFK", "LAX", "$500", "2023-12-01", "2023-12-05", "Delta")
        expected_str = "From Airport: JFK\nTo Airport: LAX\nCost: $500\nDates (Departure): 2023-12-01\nDates (Arrival): 2023-12-05\nAirlines Name: Delta"
        self.assertEqual(str(flight), expected_str)

    @patch('travel_itinerary_app.flights.requests.get')
    def test_airport_id_locator_valid(self, mock_get):
        # Test airport_id_locator with valid data
        mock_get.return_value.json.return_value = {
            "data": [
                {"navigation": {"relevantFlightParams": {"skyId": "1234", "entityId": "5678"}}}
            ]
        }
        ids = airport_id_locator("New York", "Los Angeles")
        self.assertEqual(ids, ["1234", "5678", "1234", "5678"])

    @patch('travel_itinerary_app.flights.requests.get')
    def test_airport_id_locator_invalid(self, mock_get):
        # Test airport_id_locator with invalid data
        mock_get.return_value.json.return_value = {"data": []}
        ids = airport_id_locator("InvalidCity", "AnotherInvalidCity")
        self.assertEqual(ids, ["No Data Returned, Please Try again"])

    @patch('travel_itinerary_app.flights.requests.get')
    def test_flights_finder_valid(self, mock_get):
        # Test flights_finder with valid data
        mock_get.return_value.json.return_value = {
            "data": {
                "itineraries": [
                    # Mock data for itineraries
                    # Include sample data that your API would typically return
                ]
            }
        }
        flights = flights_finder("1234", "5678", "1234", "5678", "2023-12-01", "2023-12-05")
        self.assertIsInstance(flights, list)
        self.assertTrue(all(isinstance(f, Flight) for f in flights))

   

