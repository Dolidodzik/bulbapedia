from django.shortcuts import render
from app.models import *

def homepage(request):
    # homepage_model_instance - hmi
    hmi = HomePage.objects.first()
    return render(request, "home.html", {"header": hmi.name, "text": hmi.text})

def searchpage(request, search_query):
    # Currently only name searching support, just for testing purpooses
    return render(request, "search_results.html", {"search_query": search_query, "results": Creature.objects.filter(Breed_name__contains=search_query)})

def subpage(request, creature_name):
    creature_data = Creature.objects.filter(Breed_name__iexact=creature_name).first()
    return render(request, "search_results.html", {"creature_name": creature_name, "creature_data": creature_data} )
