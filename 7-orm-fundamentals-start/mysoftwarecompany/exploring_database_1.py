import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# I want to explore the different ways to interact with the databse.
# let's import the models here.
from clients.models import Company

# reading all of the items here.
# everythig
all_companies = Company.objects.all()
# equivalent to select * no where in sql.

print(all_companies)
# you can iterate over the companies
# you can also access them like an array
first_company = all_companies[0]
# let's take a look with a breakpoint
print("Here's the values of my first company")
print(F"The id is {first_company.id}")
print(F"The name is {first_company.name}")
print(F"The email is {first_company.email}")


# Let's test how to filter items
# note objects.filter this is will return a list of matching items.
print("\n\nUsing filter")
companies_with_acme = Company.objects.filter(name="Acme Inc.")
print(F"Here's the amount of items with Acme inc. as the name {len(companies_with_acme)}")
breakpoint()


