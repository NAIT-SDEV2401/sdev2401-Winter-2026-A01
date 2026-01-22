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