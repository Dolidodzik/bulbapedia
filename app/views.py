from django.shortcuts import render
from app.models import *

def homepage(request):
    # homepage_model_instance - hmi
    hmi = HomePage.objects.first()
    return render(request, "home.html", {"header": hmi.name, "text": hmi.text})

def searchpage(request, search_query):
    data = [
        Creature.objects.filter(Breed_name__icontains=search_query),
        Creature.objects.filter(Type__icontains=search_query),
        Creature.objects.filter(Element__icontains=search_query),
        Creature.objects.filter(Frequency__icontains=search_query),
        Creature.objects.filter(Diet__icontains=search_query),
        Creature.objects.filter(Role__icontains=search_query),
        Creature.objects.filter(Endurance__icontains=search_query),
        Creature.objects.filter(Hunger__icontains=search_query),
        Creature.objects.filter(Strong_VS__icontains=search_query),
        Creature.objects.filter(Weak_VS__icontains=search_query),
        Creature.objects.filter(Attacks__icontains=search_query),
        Creature.objects.filter(Strength__icontains=search_query),
        Creature.objects.filter(Speed__icontains=search_query),
        Creature.objects.filter(Agility__icontains=search_query),
        Creature.objects.filter(Durability__icontains=search_query),
        Creature.objects.filter(Other_Enchancements__icontains=search_query),
        Creature.objects.filter(Evolves_from__icontains=search_query),
        Creature.objects.filter(Evolves_to__icontains=search_query),
        Creature.objects.filter(Fluff__icontains=search_query),
    ]

    return render(request, "search_results.html", {"search_query": search_query, "results": data })

def subpage(request, creature_name):
    creature_data = Creature.objects.filter(Role__iexact=creature_name).first()
    return render(request, "subpage.html", {"creature_name": creature_name, "creature_data": creature_data} )
