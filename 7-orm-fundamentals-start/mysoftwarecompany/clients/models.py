from django.db import models

# Important note you don't have to care how the migrations
# work, all you need to know is that it's performing
# create table and alter table commands.

# classes here that inherit from models.Model are going
# to be what's in the database.
class Company(models.Model):
    # these below are going to be the fields in the
    # database.
    name = models.CharField(max_length=100)
    # this is going to make a field in the db called
    # name with max 100 chars in size.
    email = models.EmailField(max_length=100, unique=True)
    # this is going to make a field in the db called
    # email with max 100 chars in size.
    # this is also unique.

    # Note: no need to add the id, it's added by default.


    # let's override __str__ so it's a bit nicer
    # when we print or call this.
    def __str__(self):
        return self.name
