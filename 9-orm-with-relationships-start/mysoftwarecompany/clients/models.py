from django.db import models


# our model for the client
class Company(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # company description
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    # foreign key of company on the Employees model
    # is going to give us the .employees field here.

    # if I delete a company I'll delete all employees

    def __str__(self):
        return self.name

# create a model called Role with the fields
class Role(models.Model):
    # name charfield max_length 50 unique
    name = models.CharField(max_length=50, unique=True)
    # description Textfield with blank = true
    #   and null = True
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    # core fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    # create my foreign key relationship.
    company = models.ForeignKey(
        Company, # model to relate to.
        on_delete=models.CASCADE,
        # the above just means if you delete
        # the company you delete the employees
        related_name='employees'
        # on company we'll be able to select
        # the employees with company.employees
        # this is what related name is doing.
    )
    # one more relationship (foreign key)
    # role
    role = models.ForeignKey(
        Role, # Role
        on_delete=models.SET_NULL,
        # whenever I delete a role I set
        # the this field on employee to null.
        blank=True,
        null=True, # nullable (can be null)
        related_name="employees"
        # on the Role model role.employees...
    )

    def __str__(self):
        return F"{self.first_name} {self.last_name}" \
            F" works at {self.company.name}"

