from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Checks if user is a moderator"""

    def has_permission(self, request, view):
        if request.user.groups.filter(name="moderators").exists():
            return True


class IsOwner(permissions.BasePermission):
    """Checks if user is an owner"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
