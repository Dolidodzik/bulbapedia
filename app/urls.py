from django.urls import path
from app.views import *

urlpatterns = [
    path('', homepage),
    path('search/<slug:search_query>', searchpage),
]
