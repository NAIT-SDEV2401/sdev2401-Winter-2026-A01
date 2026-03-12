from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# import form and model
from .forms import ProfileForm
from .models import Profile


# I want you to
# create the view to list all profiles
@login_required
def profile_list(request):
    profiles = Profile.objects.all()

    return render(
        request,
        "profiles/profile_list.html",
        {"profiles": profiles},
    )


# create the urls
# fix the template tags to loop through
# profiles in the template.


@login_required
def update_profile(request):
    # with the one to one mapping it will force the db
    # to have a single user to a single profile
    profile, created = Profile.objects.get_or_create(
        user=request.user,
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,  # right encoding.
            instance=profile,
        )

        if form.is_valid():
            form.save()
            return redirect("profile_edit")
    else:
        # get and other requests.
        form = ProfileForm(instance=profile)
    return render(
        request,
        "profiles/edit_profiles.html",
        {"form": form},
    )
