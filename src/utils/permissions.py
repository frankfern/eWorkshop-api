from rest_framework.permissions import BasePermission


class HasPasswordChanged(BasePermission):
    """Allow access only when the user changed the password"""

    def has_permission(self, request, view):

        return bool(request.user and request.user.profile.is_password_changed)
