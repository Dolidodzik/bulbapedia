from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def searchpage(request, search_query):
    return render(request, "search_results.html", {"search_query": search_query})
