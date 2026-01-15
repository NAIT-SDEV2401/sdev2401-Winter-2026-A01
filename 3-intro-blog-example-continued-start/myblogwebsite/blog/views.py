# render is a special django function
# that will return an html page with
# some data inside (if you want)
from django.shortcuts import render

# is going to be the controllers
# of your app (think mvc architecture)
# this is going to handle requests
# return responses

def post_list(request):
    # request we can see more of this later
