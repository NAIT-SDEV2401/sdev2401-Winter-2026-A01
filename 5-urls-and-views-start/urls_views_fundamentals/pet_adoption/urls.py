# import path from django urls
from django.urls import path

# this is where we link the url
# that the user will request
# to the app level view.

# I'm going to add the home page and
# the pet_type_details view
from .views import (
    home_page,
    pet_type_details
)
# the . is looking in the same folder
# for a file called views and a function
# called home page inside.

# we're going to make a list of paths
# which will make this connection
urlpatterns = [
    path(
        "", # is the url (here /) like default
        home_page, # this is the view
        name="home_page" # we're going to use
        # this in the templates later on.
    ),
    # we're going to make the connection
    # betwee the url path and the new view
    path(
        "pet_type/<str:pet_type>/",
        # the second part between the <>
        # defining that it's a str and
        # that you're going to pass a arg
        # called pet type
        pet_type_details,
        name="pet_type_details"
    )
]