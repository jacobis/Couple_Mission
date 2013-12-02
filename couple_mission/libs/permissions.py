from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print '123'

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsAuthenticatedOrCreateOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print '123'
        print request.method

        if request.method is 'CREATE':
            return True

        return obj.owner == request.user
