from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists() or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if view.action in ('create', 'destroy'):
            return False
        return True


class IsModerOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Модераторы').exists():
            return True

        return obj.user == request.user
