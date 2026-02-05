import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# import the Role model.

roles_data = [
    {"name": "CEO", "description": "Chief Executive Officer"},
    {"name": "Manager", "description": "Manages a team of employees"},
    {"name": "Developer", "description": "Writes code and develops software"}
]

# I want you to loop through the roles
# use get or create wit hthe data to create
# roles.
# display if it was created or selected from the db
