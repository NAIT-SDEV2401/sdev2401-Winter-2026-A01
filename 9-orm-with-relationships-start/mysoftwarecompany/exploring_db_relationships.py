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

breakpoint()