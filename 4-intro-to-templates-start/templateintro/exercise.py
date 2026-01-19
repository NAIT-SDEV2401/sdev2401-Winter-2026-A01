import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# everything above this line is needed to create a runnable django file.

import requests

# We're going to use the 8 ball api https://www.eightballapi.com/docs
# to get a reading and see if it is positive or negative
# use requests (install with pip)
# 1. hit the endpoint https://www.eightballapi.com/api to get a response.
message = requests.get("https://www.eightballapi.com/api").json() # this just fetches and parses json
breakpoint()

# 2. use the endpoint https://www.eightballapi.com/api/categories to get the categories
#    and categorize the items.
# 3. format the data
'''
{
    response: "",
    sentiment: "positive|neutral|negative"
}
'''
# 4. create a template here
'''
The 8 ball says:
YOUR_RESPONSE_HERE
the sentiment for this message is SENTIMENT_HERE

you should be happy|worried|not worried at all based on the sentiment.
'''
# 5. render the template with the context


