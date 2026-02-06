import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()
# ignore above.

from clients.models import Company, Role, Employee

new_employees_data_acme = [
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@acmetesting.com",
        "role": "CEO",
        "company": "Acme Inc.",
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@acmetesting.com",
        "role": "Manager",
        "company": "Acme Inc.",
    },
    {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@acmetesting.com",
        "role": "Developer",
        "company": "Acme Inc.",
    },

]

# for the second part.
new_employees_data_cat_sitting_int = [
    {
        "first_name": "Diana",
        "last_name": "Prince",
        "email": "diana.prince@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "CEO",
    },
    {
        "first_name": "Ethan",
        "last_name": "Hunt",
        "email": "ethan.hunt@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Manager",
    },
    {
        "first_name": "Fiona",
        "last_name": "Green",
        "email": "fiona.green@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Developer",
    },
]

# I want you to create a function that will take on arg
def create_new_employees_if_not_existing(employee_list):
    # this is the list
    # in the function
    # loop through the data.
    for employee_data in employee_list:
        # create the employees.
        company = Company.objects.get(
            name=employee_data["company"]
        )

# main function
def main():

    print("loading Acme Inc. employees")
    create_new_employees_if_not_existing(
        new_employees_data_acme
    )
# that call the above function with both lists
# call that funcition.
if __name__ == "__main__":
    main()