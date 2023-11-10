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
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        origin_city = request.POST.get('Origin City')
        destination_city = request.POST.get('Destination City')
        travelers = request.POST.get('travelers')
        min_amount = request.POST.get('min_amount')
        max_amount = request.POST.get('max_amount')

        # Create a dictionary with the form data
        form_data = {
            'departure_date': departure_date,
            'return_date': return_date,
            'origin_city': origin_city,
            'destination_city': destination_city,
            'travelers': travelers,
            'min_amount': min_amount,
            'max_amount': max_amount,
        }

        # Print the form data to the console
        print(json.dumps(form_data, indent=4))



    return render(request, 'travel_itinerary_app/processing.html')