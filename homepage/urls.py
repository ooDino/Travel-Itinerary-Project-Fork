# pages/urls.py
from django.urls import path
from .views import homePageView
from .views import resultPageView
from homepage import views

urlpatterns = [
    path("", homePageView, name="index"),
    path('filters/filter_results', resultPageView, name='filter_results'),
    path("add_filter", views.add_filter, name = "add_filter"),

]

