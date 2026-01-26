from django.contrib import admin

# import the model
from .models import Company

# this is a file that you can add your models
# to the admin sites.
admin.site.register(Company)

# for the sake of this course this is 99% of what we're
# we're goign to use for the admin, but you can
# customize it and there's a lot of customizations out ther.