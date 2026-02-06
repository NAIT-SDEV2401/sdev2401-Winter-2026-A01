import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

from clients.models import Company, Role, Employee

# select the first employee from Acme Inc.
acme_company = Company.objects.get(name="Acme Inc.")
# if the employee doesn't have a role
employee = acme_company.employees.all().first()
# .first() is handy
ceo_role = Role.objects.get(name="CEO")
if not employee.role: # employee.role this will be None
    # set the role of the employee to CEO.
    employee.role = ceo_role
    # save it!
    employee.save()
    print(F"We added {employee.role} to {employee}")
else:
    print(F"{employee} already has a role of {employee.role}")