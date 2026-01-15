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
    # what the user sent we have access to
    # a whole bunch here.

    # here in this part of the view we will
    # interact with our ORM.

    # return a response to this request
    return render(
        request,
        'blog/post_list.html'
        # the above is looking in the
        # templates folder that will be
        # aggregated on load
    )




