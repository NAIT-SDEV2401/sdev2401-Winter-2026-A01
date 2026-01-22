from django.shortcuts import render

# this is going to take in a request
# and return a response.
def home_page(request):

    # we're going to return the response
    # which will be the template for us.
    return render(
        request, # sending request as part of response
        "pet_adoption/home_page.html",
        # the above is the template
        # note don't include the "templates"
    )
