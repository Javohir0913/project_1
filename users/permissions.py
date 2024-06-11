from rest_framework.permissions import BasePermission


class IsOwnerOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        try:
            return request.user == view.get_object()
        except:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        try:
            return request.user.username == obj.username
        except:
            return False


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user.is_staff


class IsAuthenticatedOrGet(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_staff:
            return True
        elif request.method in ['PUT', 'DELETE', 'PATCH']:
            if obj.art_is_delete is False and obj.art_status is None:
                return request.user == obj.author
            return False
        return request.user.is_authenticated


class IsPostOrGet(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return True
        return False
