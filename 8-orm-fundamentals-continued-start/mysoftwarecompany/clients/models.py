from django.db import models


# our model for the client
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # let's add a description
    # we're also going to add blank=True, null=True
    # it makes less strict when you need to add something to the database.
    description = models.TextField(
        blank=True, null=True, default=""
    )
    # Two fields of the created_at and updated_at.
    created_at = models.DateTimeField(auto_now_add=True)
    # this is going to capture the date when you initially created the model.
    updated_at = models.DateTimeField(auto_now=True)
    # these are not nullable. if I have something in the database
    # I need to provide some type of one off.

    def __str__(self):
        return self.name


'''

    # date fields
    # the auto_now_add Automatically set the date when the record is created
    date_joined = models.DateField(auto_now_add=True)
    # the
    updated_at = models.DateField(auto_now=True)

'''