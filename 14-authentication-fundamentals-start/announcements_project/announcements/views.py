from django.shortcuts import render, redirect

# let's import the login_required decorator.
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Announcement

# everyone can see if they're logged in.
@login_required
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(
        request,
        'announcements/announcement_list.html',
        {'announcements': announcements}
    )

# restricted to teachers.
def create_announcement(request):
    return render(request, 'announcements/create_announcement.html')
