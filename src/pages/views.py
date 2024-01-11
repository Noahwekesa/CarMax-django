from django.shortcuts import render

from pages.models import Listing


def landing_view(request):
    context = {}
    return render(request, "pages/index.html", context)


def list_cars(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, "pages/home.html", context)
