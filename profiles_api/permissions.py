from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Check and Allow user to edit their own profile."""
    def has_object_permission(self, request, view, obj):
        """Overriding original method with our own"""
        if request.method in permissions.SAFE_METHODS: return True
        # The above statement checks if the requested method is actually one of the safe methods (Get, retrieve, list, where no editing is done.)
        return obj.id == request.user.id # else if editable request is presented, return true if account is his own.

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id