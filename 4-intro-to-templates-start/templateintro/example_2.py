import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# everything above this line is needed to create a runnable django file.

from django.template import Template, Context

data = {
    "rating_topic": "Book",
    "best_rating": 5,
    "worst_rating": 1,
    "items": [
        {"title": "brave new world", "rating": 4},
        {"title": "1984",  "rating": 5},
        {"title": "The Great Gatsby", "rating": 4},
        {"title": "Twilight", "rating": 1},
    ]
}

# create a template in this format
'''
Books:
- title_here (rating)
- title_here (rating)
- title_here (rating)
'''

# 1. create a template
template = Template("""
Books:
{% for book in items %}
- {{ book.title | title }} ({{ book.rating }}) {% if book.rating >= 4 %}Great book!{% else %}It was okay{% endif %}
{% endfor %}
""")
# Just a note here in the above make sure your template tags have space around the items.
# {% for ... %} and {% endfor %} need spaces around percentage signs, pipes and variables
# {% if ... %} {% endif %} always needs a closing tag.
# | allow you to modify the data You can add more here as well.

# 2. create a context
context = Context(data)
# 3. render it.
print(template.render(context))
