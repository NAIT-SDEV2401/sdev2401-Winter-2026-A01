from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import BulkAssignmentUploadForm


# make the bulk_assignment_upload view
# using the form we've created.
@login_required
def bulk_assignment_upload(request):
    if request.method == "POST":
        form = BulkAssignmentUploadForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            csv_file = form.cleaned_data.get("csv_file")

            # below we're going to handle the parsing of
            # the data.

    else:

        form = BulkAssignmentUploadForm()
    return render(
        request,
        "courses/bulk_assignment_upload.html",
        {"form": form},
    )
