from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('own')
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.made_by == request.user