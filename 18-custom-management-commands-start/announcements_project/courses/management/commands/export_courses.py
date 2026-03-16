import csv
from django.core.management.base import BaseCommand

from courses.models import Course


# create management command
class Command(BaseCommand):
    help = "Exports courses to a csv file"

    # that takes output_file as an argument
    def add_arguments(self, parser):
        parser.add_argument(
            "output_file", type=str, help="Path to output csv course file"
        )

    def handle(self, *args, **kwargs):
        output_file = kwargs.get("output_file")

        # errors if it doesn't have it.
        if not output_file:
            self.stdout.write(
                self.style.ERROR(
                    "Please provide an output file",
                )
            )

        # we're going to get all of the courses
        courses = Course.objects.all()
        # I want you to create a csv with all of the courses
        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            # add the header line
            writer.writerow(["course title", "course description"])
            # loop through courses and add them to the csv.
            for course in courses:
                writer.writerow([course.title, course.description])

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully exported {courses.count()} to {output_file}"
                )
            )

        # name and description.
