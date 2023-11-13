from django.shortcuts import render


# travel_itinerary_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import TravelPlan
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
# travel_itinerary_app/views.py
from django.shortcuts import render
from .flights import airport_id_locator, flights_finder
from datetime import datetime

def home(request):
    # Your logic for the homepage view
    return render(request, 'travel_itinerary_app/home.html')


def signup(request):
    return render(request, 'travel_itinerary_app/signup.html')

def login_view(request):
    return render(request, 'travel_itinerary_app/login.html')

# @login_required
# def plan_trip(request):
#     # Implement your view logic for planning a trip here
#     return render(request, 'travel_itinerary_app/plan_trip.html')

@login_required
def itinerary(request):
    return render(request, 'travel_itinerary_app/itinerary.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage or another desired page upon successful signup
    else:
        form = SignupForm()
    return render(request, 'travel_itinerary_app/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or another desired page upon successful login
    else:
        form = LoginForm()
    return render(request, 'travel_itinerary_app/login.html', {'form': form})



from .models import Trip, ItineraryItem  # Import your models

def profile(request):
    user = request.user  # Get the logged-in user
    past_trips = Trip.objects.filter(user=user)
    current_itinerary = ItineraryItem.objects.filter(user=user)

    context = {
        'user': user,
        'past_trips': past_trips,
        'current_itinerary': current_itinerary,
    }

    return render(request, 'travel_itinerary_app/profile.html', context)


def itinerary_form(request):
    if request.method == 'POST':
        # Retrieve form data
        departure_date_str = request.POST.get('departure_date')
        departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        return_date_str = request.POST.get('return_date')
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")

        origin_city = request.POST.get('Origin City')
        destination_city = request.POST.get('Destination City')
        travelers = request.POST.get('travelers')
        min_amount = request.POST.get('min_amount')
        max_amount = request.POST.get('max_amount')


        #airport id locator
        try :
            airport_ids = airport_id_locator(origin_city,destination_city)
            if isinstance(airport_ids, str):
                error_message = airport_ids
                return render(request, 'travel_itinerary_app/error_page.html', {'error_message': error_message})
            origin_sky_id = airport_ids[0]
            destination_sky_id = airport_ids[2]
            origin_entity_id = airport_ids[1]
            destination_entity_id = airport_ids[3]
        except :
            return render(request, 'travel_itinerary_app/error_page.html', {'error_message': 'No Airport ID Found'})

        # print(airport_ids)
        # # print("origin id is:")
        # # print(airport_ids[0])
        # # print("destination  id is:")
        # # print(airport_ids[1])
        # # Print the form data to the console

        #finding the flights
        try:
            flight_objects = flights_finder(origin_sky_id,destination_sky_id,origin_entity_id,
                                 destination_entity_id,departure_date,return_date,travelers)
            if isinstance(flight_objects, str):
                error_message = flight_objects  # Use the error message from the helper function
                print("Error in flights_finder:", error_message)  # Print the error message
                return render(request, 'travel_itinerary_app/error_page.html', {'error_message': error_message})
        except :
            return render(request, 'travel_itinerary_app/error_page.html', {'error_message': 'Couldnt Find Any Flights'})

        if flight_objects and len(flight_objects) > 0:
            flights = len(flight_objects)
            print(f'Total {flights} flights found for your trip')
            for i in range(len(flight_objects)):
                print(f"\nFlight {i + 1} info : ")
                print(flight_objects[i])


        else:
            return render(request, 'travel_itinerary_app/error_page.html',
                          {'error_message': 'Couldnt Find Any Flights'})



        # print(flight_objects[0].from_airport)






    return render(request, 'travel_itinerary_app/processing.html')