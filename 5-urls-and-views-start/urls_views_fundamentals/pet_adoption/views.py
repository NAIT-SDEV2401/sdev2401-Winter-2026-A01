from django.shortcuts import render

# over here we have a dictionary of values.
PET_TYPES = {
    'dog': {
        'name': 'Dog',
        'traits': 'Loyal, energetic, needs space and exercise.',
        'lifestyle_fit': 'active'
    },
    'cat': {
        'name': 'Cat',
        'traits': 'Independent, cuddly, low-maintenance.',
        'lifestyle_fit': 'quiet'
    },
    'rabbit': {
        'name': 'Rabbit',
        'traits': 'Gentle, small, requires calm environment.',
        'lifestyle_fit': 'quiet'
    },
    'parrot': {
        'name': 'Parrot',
        'traits': 'Social, intelligent, needs stimulation.',
        'lifestyle_fit': 'social'
    }
}

# this is going to take in a request
# and return a response.
def home_page(request):
    # we're going to create a variablle
    name = "Humane Society"

    # we're going to return the response
    # which will be the template for us.
    return render(
        request, # sending request as part of response
        "pet_adoption/home_page.html",
        # the above is the template
        # note don't include the "templates"
        {
            "name": name,
            "pet_types": PET_TYPES
        }
        # this line above passes the data
        # as context to the template
    )

# below we have another parameter
# that's going to be passed in from the url.
def pet_type_details(request, pet_type):

    return render(
        request, # passing the request to the response
        "pet_adoption/pet_detail.html" # the template
    )






