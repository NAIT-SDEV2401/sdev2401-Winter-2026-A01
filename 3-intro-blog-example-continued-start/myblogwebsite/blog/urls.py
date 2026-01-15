# map the url to a django view
# the line below is going to
# create the mapping of
# url to view.
from django.urls import path

# below we're importing the views
from . import views
# this is at the app level for blog
urlpatterns = [
    path("", views.post_list, name="post_list")
]



