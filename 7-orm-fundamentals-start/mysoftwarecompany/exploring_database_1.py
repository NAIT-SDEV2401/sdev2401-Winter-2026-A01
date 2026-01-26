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

print(all_companies)
# you can iterate over the companies
# you can also access them like an array
first_company = all_companies[0]
# let's take a look with a breakpoint
print("Here's the values of my first company")
print(F"The id is {first_company.id}")
print(F"The name is {first_company.name}")
print(F"The email is {first_company.email}")


# breakpoint()
