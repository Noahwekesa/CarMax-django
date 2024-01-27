from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from pages.filters import ListingFilter
from pages.forms import ListingForm
from django.contrib import messages

from pages.models import Listing
from users.forms import LocationForm


def landing_view(request):
    context = {}
    return render(request, "pages/index.html", context)


def list_cars(request):
    listings = Listing.objects.all().order_by('-created_at')
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listing_filter': listing_filter
    }
    return render(request, "pages/home.html", context)


@login_required
def post_car(request):
    if request.method == 'POST':
        try:
            p_form = ListingForm(request.POST, request.FILES)
            l_form = LocationForm(request.POST)
            if p_form.is_valid and l_form.is_valid():
                listing = p_form.save(commit=False)
                l_form = l_form.save()
                listing.seller = request.user.profile
                listing.location = l_form
                listing.save()
                messages.info(
                    request, f'{listing.model} was Posted Successfully! ')
                return redirect('list')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(request, 'An error occured while posting your car')
    elif request.method == 'GET':
        p_form = ListingForm()
        l_form = LocationForm()
    context = {
        'p_form': p_form,
        'l_form': l_form
    }
    return render(request, 'pages/PostCarForm.html', context)


def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        context = {
            'listing': listing
        }
        return render(request, 'pages/listing.html', context)
    except Exception as e:
        messages.error(request, f'invalid UID {id} was provided for listing')
        return redirect('list')
