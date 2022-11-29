from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def templateView(request, *args, **kwargs):
    return render(request, "index.html", {})


def portfolioView(request, *args, **kwargs):
    return render(request, "portfolio-details.html", {})