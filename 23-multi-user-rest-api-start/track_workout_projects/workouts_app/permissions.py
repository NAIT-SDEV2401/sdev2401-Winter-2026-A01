# IMPORTANT these permissions should be in probably a core folder
# where the authentication/custom user would lie.
# because you want to share them across apps.

# we're going to use this permission and override it.
from rest_framework.permissions import IsAuthenticated


# in this permission we're going to say if a user is trying to modify a workout log
# it should only be that user.
class IsOwnerOfResourceOrReadOnly(IsAuthenticated):
    """
    Custom permission to allow owners of an object to edit it.
    This assumes that a model has a `user` attribute.
    """

    # this returns a boolean whether they have permission or not.
    def has_object_permission(self, request, view, obj):
        # Read permissions on any request.
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return
