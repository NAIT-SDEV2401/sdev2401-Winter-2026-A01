import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# let's import the tables
from clients.models import Employee, Company

COMPANY_NAME = "Acme Inc."
# get an instance
acme_company = Company.objects.get(
    name=COMPANY_NAME
)

# let's get the employees from the acme_company instance
all_employees = acme_company.employees.all()

# another way to get all employees
all_employees = Employee.objects.filter(
    company=acme_company # instance
)
# both of these ways do the same thing
print("All employees")
print(all_employees)

# let's create an employee
new_employee = Employee.objects.create(
    # core fields
    first_name="Rick",
    last_name="Steves",
    email="rick@test.com",
    # relationship will take an instance
    company=acme_company
)

