from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    # User re_path to allow spaces in names
    re_path(r'^creature/(?P<creature_name>[\w|\W]+)', subpage),
    path('advanced_search/', AdvancedSearchView.as_view()),
]
