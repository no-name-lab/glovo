from rest_framework import permissions
from rest_framework.permissions import BasePermission


# Клиенты могут оформлять заказы и просматривать свои заказы.

class CheckReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.client == request.user


# Курьеры могут видеть доступные заказы и изменять их статус.

class CheckCourier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.courier == request.user or obj.status == 'available'

# Владельцы магазинов могут просматривать и управлять заказами, связанными с их магазинами

class CheckStoreOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_store:
            return True
        return False


# Администраторы могут управлять всеми заказами и назначать курьеров.

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'