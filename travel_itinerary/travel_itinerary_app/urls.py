# travel_itinerary_app/urls.py
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('itinerary_form/', views.itinerary_form, name='itinerary_form'),
    path("search_results/", views.search_results, name="search_results"),
    # Add more URL patterns as needed
]

