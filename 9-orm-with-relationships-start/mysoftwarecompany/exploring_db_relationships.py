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
# the lines below will return the same as the above.
# you can filter across the relationship with MODEL__FIELD in the filter.
all_employees = Employee.objects.filter(
    company__email="acme@testing.com"
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
print("new_employee")
print(new_employee)

# another_employee = Employee(
#     first_name="Gary",
#     last_name="the guy",
#     email="garay@test.com",
#     company=acme_company,
# )
# # the above gives an instance of employee
# # but it's not committed to the database yet
# another_employee.save()
# # this line above will commit it to the db.
# print("another_employee")
# print(another_employee)


