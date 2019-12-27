from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('search/<slug:search_query>/', searchpage),
    #path('creature/<slug:creature_name>/', subpage),
    re_path(r'^creature/(?P<creature_name>[\w|\W]+)', subpage),
    path('advanced_search/', AdvancedSearchView.as_view()),
]
