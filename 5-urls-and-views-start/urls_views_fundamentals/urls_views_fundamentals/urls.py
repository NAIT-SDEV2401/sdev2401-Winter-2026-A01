from django.contrib import admin
# where we're going to use include for the app
from django.urls import path, include

# this project level urls
urlpatterns = [
    path("admin/", admin.site.urls),
    # we're going to include the app level urls
    path("", include("pet_adoption.urls")),
    # pet_adoption.urls above is looking for
    # the urls file inside of the pet_adoption
    # app (needs to be added to INSTALLED_APPS in settings)
]
