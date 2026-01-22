# import path from django urls
from django.urls import path

# this is where we link the url
# that the user will request
# to the app level view.

# to do I need to import the view
from .views import home_page
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
    )
]