from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
