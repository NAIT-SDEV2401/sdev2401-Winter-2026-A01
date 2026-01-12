from django.contrib import admin

# we're going import our models in this file.
from .models import Post

# and "register" them on the admin so we can
# browse them.
admin.site.register(Post)
