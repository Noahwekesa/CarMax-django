from django.shortcuts import render


def landing_view(request):
    context = {}
    return render(request, "pages/index.html", context)
