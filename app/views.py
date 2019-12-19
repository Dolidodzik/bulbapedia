from django.shortcuts import render, redirect
from app.models import *
from django.views import View
from app.forms import CreatureForm

def homepage(request):
    # homepage_model_instance - hmi
    hmi = HomePage.objects.first()
    return render(request, "home.html", {"header": hmi.name, "text": hmi.text})


def searchpage(request, search_query):

    results_dict = dict()
    for field in Creature._meta.get_fields():
        if search_query:
            field_name_icontains = field.name + '__icontains'
            qs = Creature.objects.filter(**{ field_name_icontains: search_query })
            for row in qs:
                results_dict[ row.id ] = row

    results = []
    for x in results_dict:
        results.append( results_dict[x] )

    return render(request, "search_results.html", {"search_query": search_query, "results": results })

def subpage(request, creature_name):
    creature_data = Creature.objects.filter(Role__iexact=creature_name).first()
    return render(request, "subpage.html", {"creature_name": creature_name, "creature_data": creature_data} )

class AdvancedSearch(View):
    template_name = 'advanced_search.html'

    def get(self, request):
        form = CreatureForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CreatureForm(request.POST)
        results_dict = dict()

        if form.is_valid():
            cd = form.cleaned_data
            for field in Creature._meta.get_fields():
                user_input = cd.get(field.name)
                if user_input:
                    field_name_icontains = field.name + '__icontains'
                    qs = Creature.objects.filter(**{ field_name_icontains: user_input })
                    for row in qs:
                        results_dict[ row.id ] = row
        results = []
        for x in results_dict:
            results.append( results_dict[x] )

        return render(request, self.template_name, {"form": form, "results": results})
