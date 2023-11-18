import json
import requests


api_key = "a7519fd6bemsh8ab2c1389673efcp128997jsn513b4aa85669"


class Flight:
    def __init__(
        self,
        from_airport,
        to_airport,
        cost,
        dates_departure,
        dates_arrival,
        airlines_name,
    ):
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.cost = cost
        self.dates_departure = dates_departure
        self.dates_arrival = dates_arrival
        self.airlines_name = airlines_name

    def __str__(self):
        return (
            f"From Airport: {self.from_airport}\n"
            f"To Airport: {self.to_airport}\n"
            f"Cost: {self.cost}\n"
            f"Dates (Departure): {self.dates_departure}\n"
            f"Dates (Arrival): {self.dates_arrival}\n"
            f"Airlines Name: {self.airlines_name}"
        )


# This Method  Extracts City name from the itinerary form and finds the airport id via api call
def airport_id_locator(origin, destination):
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

    querystring = {"query": f"{origin}"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    try:
        origin_airport_skyId = data["data"][0]["navigation"]["relevantFlightParams"][
            "skyId"
        ]
        origin_airort_entityId = data["data"][0]["navigation"]["relevantFlightParams"][
            "entityId"
        ]
    except:
        return ["No Data Returned, Please Try again"]

    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

    querystring = {"query": f"{destination}"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    try:
        destination_airport_skyId = data["data"][0]["navigation"][
            "relevantFlightParams"
        ]["skyId"]
        destination_airort_entityId = data["data"][0]["navigation"][
            "relevantFlightParams"
        ]["entityId"]
    except:
        return ["No Data Returned, Please Try again"]

    # print(origin_airport_id,destination_airport_id)
    airport_ids = [
        origin_airport_skyId,
        origin_airort_entityId,
        destination_airport_skyId,
        destination_airort_entityId,
    ]

    return airport_ids


def flights_finder(
    originSkyId,
    destinationSkyId,
    originEntityId,
    destinationEntityId,
    departure_date,
    arrival_date,
    adults=1,
):
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"

    querystring = {
        "originSkyId": originSkyId,
        "destinationSkyId": destinationSkyId,
        "originEntityId": originEntityId,
        "destinationEntityId": destinationEntityId,
        "date": departure_date,
        "returnDate": arrival_date,
        "currency": "USD",
        "market": "en-US",
        "countryCode": "US",
        "adults": adults,
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    try:
        itineraries = data["data"]["itineraries"]
    except:
        return ["No Itinerary Found, Please Try Again"]

    # Extract data for the first 3 flights and create Flight objects
    flight_objects = []
    number_of_itineraries = 5 if len(itineraries) >= 5 else len(itineraries)

    for i in range(number_of_itineraries):  # Loop through the first 3 itineraries
        itinerary = itineraries[i]
        from_airport = itinerary["legs"][0]["origin"]["name"]
        to_airport = itinerary["legs"][0]["destination"]["name"]
        cost = itinerary["price"]["formatted"]
        dates_departure = itinerary["legs"][0]["departure"]
        dates_arrival = itinerary["legs"][0]["arrival"]
        airlines_name = itinerary["legs"][0]["carriers"]["marketing"][0]["name"]

        flight_info = Flight(
            from_airport,
            to_airport,
            cost,
            dates_departure,
            dates_arrival,
            airlines_name,
        )
        flight_objects.append(flight_info)

    return flight_objects
