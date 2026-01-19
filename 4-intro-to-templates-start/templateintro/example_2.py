import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")


from django.template import Template, Context

data = {
    "rating_topic": "Book",
    "best_rating": 5,
    "worst_rating": 1,
    "items": [
        {"title": "Brave New World", "rating": 4},
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
- {{ book.title }} ({{ book.rating }})
{% endfor %}
""")
# 2. create a context
context = Context(data)
# 3. render it.
print(template.render(context))
