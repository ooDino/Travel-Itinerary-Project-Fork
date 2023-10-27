# pages/urls.py
from django.urls import path
from homepage import views
from homepage.views import homePageView

urlpatterns = [
    path(
        "", homePageView, name="homepage"
    ),  # just to test out if my website is working :D
    path("search_results/", views.search_results, name="search_results"),  # test 2
]
