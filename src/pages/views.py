from django.shortcuts import render


def landing_view(request):
    context = {}
    return render(request, "pages/index.html", context)


def list_cars(request):
    context = {
    }
    return render(request, "pages/list.html", context)
