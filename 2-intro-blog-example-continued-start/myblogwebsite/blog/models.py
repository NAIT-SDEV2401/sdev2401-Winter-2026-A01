from django.conf import settings
from django.db import models
from django.utils import timezone

'''
To apply this model to the database.

We need to run two commands
1. python manage.py makemigrations
    - This is going to generate a code file that if ran will
    apply the table to the database.
2. python manage.py migrate
    - This is going to run the code file(s) above


'''

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
