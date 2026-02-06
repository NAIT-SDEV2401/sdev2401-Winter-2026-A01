import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# select the first employee from Acme Inc.
# if the employee doesn't have a role
# set the role of the employee to CEO.

