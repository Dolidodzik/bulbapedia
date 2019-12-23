from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('search/<slug:search_query>/', searchpage),
    path('creature/<slug:creature_name>/', subpage),
    path('advanced_search/', AdvancedSearchView.as_view()),
]
