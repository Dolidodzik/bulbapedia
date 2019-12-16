from django.shortcuts import render
from app.models import *

def homepage(request):
    # homepage_model_instance - hmi
    hmi = HomePage.objects.first()
    return render(request, "home.html", {"header": hmi.name, "text": hmi.text})

def searchpage(request, search_query):
    return render(request, "search_results.html", {"search_query": search_query})
