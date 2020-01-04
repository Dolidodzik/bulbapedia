from django.shortcuts import render, redirect
from app.models import *
from django.views import View
from app.forms import CreatureForm
from django.http import JsonResponse
from django.core import serializers
import json

def search(request):
    search_query = request.GET.get("search_query", None)
    advanced_search_query = request.GET.get("advanced_search_query", None)

    if search_query or advanced_search_query:
        # Using dict instead of list to avoid reapeting the same result
        results_dict = dict()
        results = []
        if search_query:
            search_query_parts = search_query.split('AMPERSAND_MARK')
            creature_filelds = Creature._meta.get_fields()

            for search_query_part in search_query_parts:
                for field in creature_filelds:
                    # Getting results and assigning it to dict
                    field_name_icontains = field.name + '__icontains'
                    qs = Creature.objects.filter(**{ field_name_icontains: search_query_part.strip() })
                    for row in qs:
                        results_dict[ row.id ] = row
        elif advanced_search_query:
            inputs_string = advanced_search_query
            inputs_list = list(inputs_string.split(","))
            for i, field in enumerate(Creature._meta.get_fields()):
                # Skip first 3 fields (id, created_date, modified_date)
                if  i >= 3:
                    user_input = inputs_list[i-3]
                    if user_input:
                        # Getting results and assigning it to dict
                        field_name_icontains = field.name + '__icontains'
                        qs = Creature.objects.filter(**{ field_name_icontains: user_input })
                        for row in qs:
                            results_dict[ row.id ] = row

        # Converting dict to list
        for x in results_dict:
            results.append( serializers.serialize('json', [results_dict[x]] ))

        # Last index of list will be that was user input previously
        results.append(search_query)
        return results

class HomePageView(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name, {"home": HomePage.objects.first(), "form": CreatureForm(), "search": json.dumps(search(request)) })

class AdvancedSearchView(View):
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

def subpage(request, creature_name):
    creature_data = Creature.objects.filter(Breed_name=creature_name).first()
    return render(request, "subpage.html", {"creature_name": creature_name, "creature_data": creature_data, "form": CreatureForm(), "search_results": json.dumps(search(request)) })
