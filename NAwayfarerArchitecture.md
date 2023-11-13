# Nawayfarer Architecture

## 1) High-level Component Diagram 

![High Level Component Diagram] (highlevelcomponentdiagramNWayfarer.png)

This segment of the documentation regards the High-Level Component Diagram of NAwayfarer as of 11/13/2023
This is just a BETA of our application, please bare in mind it is still quite basic.

Summary of the High-level Component Diagram:

The browser is acting as a user interface where the user will interact with the application. Since we are running this locally (not set up on cloud yet), the UI is connected by a local development server. The user interface allows users to login through the use of our authentication on the application. The user info is confirmed and authentication is complete. With that, the application uses the backend to call (from views) our APIs through a GET request; the API's are the Yelp and Kiwi API as of now.

NOTE: soon it will include OpenAI's API as well, but as mentioned before, this is still IN BETA. 

The API results are then returned to the backend, and then used in the beta version of our itinerary creation, where the results are now displayed (both flight information and hotel information of an area). The result is of course displayed in the user interface, where users will be able to look at the result that was brought up by the itinerary creation tool.

NOTE: This will still be updated, as our results have yet to be stored, and we have yet to fully create a real itinerary for users. Additionally, we are planning to use at least one more API to complete our application. 

DATE: Updated as of 11/13/2023