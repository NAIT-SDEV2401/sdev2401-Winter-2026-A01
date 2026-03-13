import csv

from django.db import models
from django.conf import settings

# using time in django.
from django.utils import timezone


# create an assignment model
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignments"
    )

    def __str__(self):
        return self.title

    # cls is Assignment class itself.
    @classmethod
    def create_assignments_from_file(cls, csv_file, owner):
        # decode the file
        breakpoint()
        # ensure that you add you .splitlines()
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        # use the csv dict reader to read this.
        reader = csv.DictReader(decoded_file)
        assignments = []

        # loop through the rows
        # each row will look like this:
        # {'title': 'Assignment 1', 'description': 'Introduction to Python', 'date': '2026-02-10', 'time': '09:00'}
        for row in reader:
            # create the assignment and store it.
            new_assignment, created = Assignment.objects.get_or_create(
                title=row.get("title"),
                description=row.get("description"),
                due_date=timezone.now(),
                owner=owner,
            )
            # append to assignemtns
            if created:
                assignments.append(new_assignment)

        return assignments


# create a submission model
# - assignment: foreign key (use cascade)
# - student: name
# - file: filefield (upload to "submissions/")
# - subitted_at: DateTimeField when its' created.
class Submission(models.Model):
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="submissions",
    )
    student_name = models.CharField(max_length=100)

    file = models.FileField(upload_to="submissions/")
    # inside of media this will uplaod to "submissions/"
    # we need to confirm we have the MEDIA_ROOT and MEDIA_URL

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student_name} for {self.assignment}"
