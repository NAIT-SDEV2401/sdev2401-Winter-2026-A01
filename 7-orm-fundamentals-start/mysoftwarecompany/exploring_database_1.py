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
# note this will return a list of items.
print(F"Here's the amount of items with Acme inc. as the name {len(companies_with_acme)}")

# let's use get
company_at_id_two = Company.objects.get(id=2) # if there's no item there.
# this returns a single item here
print(F"company at id 2 is: {company_at_id_two}")
# note get will throw an error if not found

# two mins - use .get to get the company of rick and garys bbq.
# display name and email in a string.
rick_and_garys_company = Company.objects.get(
    # i can get on any field.
    name="rick and garys bbq"
)

print(F"BEST BBQ: {rick_and_garys_company.name} \n contact at {rick_and_garys_company.email}")

# print("CREATE IN THE DATABASE")
# .objects.create is going to be INSERT INTO
# new_company = Company.objects.create(
#     name="Dog Walking co",
#     email="dog@test.com"
# )

# get or create is handy because you can always fetch the record (if it's create or not)
# syntax returns first the object and second a boolean if it was created.
# company_four, created= Company.objects.get_or_create(
#     name="Dans Cat Meowing Competition",
#     email="danscats@test.com"
# )
# breakpoint()
# print(F"the value from {company_four}")
# print(company_four)
# print(F"created {created}")

# Let's talk about updating
# update table where ... in SQL

company_to_update = Company.objects.get(id=5)
breakpoint()
# reassign the fields on the company
company_to_update.name = "Steve's Dunking Co"
company_to_update.email = "Steve@test.com"
# save commits the changes to database
company_to_update.save()

# deleting.
company_to_update.delete()
