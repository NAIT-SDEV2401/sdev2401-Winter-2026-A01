from django.shortcuts import render, redirect
# we are using these two functions to authenticate a user.
from django.contrib.auth import login, authenticate

# import AuthenticationForm built in django.
from django.contrib.auth.forms import AuthenticationForm

# import our new form here
from .forms import UserRegistrationForm

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # check if valid.
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # perform the check to see if the user exists
            # with authenticate.
            user = authenticate(request,
                                username=username,
                                password=password)
            # returns a user if they exist or none.
            # check if the user existists we're going login
            # as the user and redirect them to the announcements
            # page.
            if user is not None:
                login(request, user)
                return redirect('announcement_list')

    else:
        form = AuthenticationForm()
    return render(
        request,
        "core/login.html",
        { "form": form }
    )


# let's create the view to register a user
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() # save the new user to the database
            login(request, user)

            # redirect the user on successful form submission to
            # the annoucements list
            return redirect("announcement_list")
            # where "announcement_list" is the name of the url
            # to redirect to.
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'core/register.html',
        { "form": form }
    )