from django.urls import path

# import the views.
from .views import list_companies

urlpatterns = [
    path("", list_companies, name="companies_list"),
]