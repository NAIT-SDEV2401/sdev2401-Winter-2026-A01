# render is a special django function
# that will return an html page with
# some data inside (if you want)
from django.shortcuts import render
# import the model
from .models import Post

# is going to be the controllers
# of your app (think mvc architecture)
# this is going to handle requests
# return responses
def post_list(request):
    # request we can see more of this later
    # what the user sent we have access to
    # a whole bunch here.

    # let's get the posts
    # below is like (select * from post)
    posts = Post.objects.all()
    # I want you to put a breakpoint here
    # breakpoint()
    # handy breakpoint commands
    # l or ll show where you are
    # c continue
    # n next

    # return a response to this request
    return render(
        request,
        'blog/post_list.html',
        {
            "title": "Hello I'm using a backend framework",
            "posts": posts
        }
        # the above is sending context
        # which is data to the template
    )




