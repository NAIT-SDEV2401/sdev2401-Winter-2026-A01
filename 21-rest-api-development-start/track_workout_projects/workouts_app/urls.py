# import django urls path
from django.urls import path

from .views import ExerciseAPIView

urlpatterns = [
    # for the list and create view.
    path(
        "exercises/",
        ExerciseAPIView.as_view(),
        name="exercise-api",
    ),
    # we need to add a new path for the
    # detail, put/patch and delete view.
    path(
        "exercises/<int:id>",
        ExerciseAPIView.as_view(),
        name="exercise-api",
    ),
]
