from django.shortcuts import render
from app.models import *

def homepage(request):
    # homepage_model_instance - hmi
    hmi = HomePage.objects.first()
    return render(request, "home.html", {"header": hmi.name, "text": hmi.text})

def searchpage(request, search_query):
    # Currently only name searching support
    return render(request, "search_results.html", {"search_query": search_query, "results": Creature.objects.filter(Breed_name__contains=search_query)})
