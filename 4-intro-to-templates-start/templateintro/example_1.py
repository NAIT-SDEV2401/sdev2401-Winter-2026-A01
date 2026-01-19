import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")

from django.template import Template, Context



# you have some data in dictionary
data = {
    "rating_topic": "movie",
    "best_rating": 10,
    "worst_rating": 0,
}

# where we render
template = Template("""
 {{ rating_topic }} will have ratings from {{ best_rating }} to {{ worst_rating }}
 where {{ best_rating }} is the best.
""")

# the data dictions to the context object
context = Context(data)

# some other context.
second_context = Context({
    "rating_topic": "Books",
    "best_rating": 5,
    "worst_rating": 1
})


# just render it with the new item here.
print(template.render(context))


# render the second
print(template.render(second_context))