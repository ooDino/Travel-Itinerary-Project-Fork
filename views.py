from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .yelp_api import search_businesses

# Create your views here.


def homePageView(request):
    return HttpResponse("Hello, World!")


def search_results(request):
    term = request.GET.get("term", "")
    location = request.GET.get("location", "")
    context = {
        "businesses": [],
        "error_message": "",
        "term": term,
        "location": location,
    }

    try:
        results = search_businesses(term, location)
        context["businesses"] = results.get("businesses", [])
    except Exception as e:
        context["error_message"] = "Sorry, there was an error processing your request."

    return render(request, "homepage/search_results.html", context)
