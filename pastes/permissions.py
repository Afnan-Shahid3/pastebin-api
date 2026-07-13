from rest_framework import permissions

class IsOwnerOrPublicReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

        if not obj.is_private and request.method in permissions.SAFE_METHODS:
            return True
        
        return False


        