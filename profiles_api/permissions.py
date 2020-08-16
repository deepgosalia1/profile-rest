from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Check and Allow user to edit their own profile."""
    def has_object_permission(self, request, view, obj):
        """Overriding original method with our own"""
        if request.method in permissions.SAFE_METHODS: return True
        # The above statement checks if the requested method is actually one of the safe methods (Get, retrieve, list, where no editing is done.)
        return obj.id == request.user.id # else if editable request is presented, return true if account is his own.