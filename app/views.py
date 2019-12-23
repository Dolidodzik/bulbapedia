from django.shortcuts import render, redirect
from app.models import *
from django.views import View
from app.forms import CreatureForm

class HomePageView(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name, {"home": HomePage.objects.first(), "form": CreatureForm()})

def searchpage(request, search_query):
    if search_query:
        # Using dict instead of list to avoid reapeting the same result
        results_dict = dict()
        for field in Creature._meta.get_fields():
            # Getting results and assigning it to dict
            field_name_icontains = field.name + '__icontains'
            qs = Creature.objects.filter(**{ field_name_icontains: search_query })
            for row in qs:
                results_dict[ row.id ] = row

    # Converting dict to list
    results = []
    for x in results_dict:
        results.append( results_dict[x] )

    return render(request, "search_results.html", {"search_query": search_query, "results": results })

def subpage(request, creature_name):
    creature_data = Creature.objects.filter(Breed_name=creature_name).first()
    return render(request, "subpage.html", {"creature_name": creature_name, "creature_data": creature_data} )

class AdvancedSearchView(View):
    template_name = 'advanced_search.html'

    def get(self, request):
        form = CreatureForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CreatureForm(request.POST)
        # Using dict instead of list to avoid reapeting the same result
        results_dict = dict()

        if form.is_valid():
            cd = form.cleaned_data
            for field in Creature._meta.get_fields():
                user_input = cd.get(field.name)
                if user_input:
                    # Getting results and assigning it to dict
                    field_name_icontains = field.name + '__icontains'
                    qs = Creature.objects.filter(**{ field_name_icontains: user_input })
                    for row in qs:
                        results_dict[ row.id ] = row
        # Converting dict to list
        results = []
        for x in results_dict:
            results.append( results_dict[x] )

        return render(request, self.template_name, {"form": form, "results": results})
