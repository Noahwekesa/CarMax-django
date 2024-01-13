from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import redirect, render
from pages.forms import ListingForm

from pages.models import Listing
from users.forms import LocationForm


def landing_view(request):
    context = {}
    return render(request, "pages/index.html", context)


def list_cars(request):
    listings = Listing.objects.all().order_by('-created_at')
    context = {
        'listings': listings
    }
    return render(request, "pages/home.html", context)


@login_required
def post_car(request):
    p_form = ListingForm()
    l_form = LocationForm()
    context = {
        'p_form': p_form,
        'l_form': l_form
    }
    return render(request, 'pages/PostCarForm.html', context)
