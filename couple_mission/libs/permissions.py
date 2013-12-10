# -*- coding: utf-8 -*-

from rest_framework import permissions

from couple_mission.apps.couple.controller import CoupleController


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsOwnerOrCoupleOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        is_owner = bool(obj.user == request.user)
        is_couple = bool(CoupleController.get_couple(request.user))

        print is_owner
        print is_couple

        return is_owner or is_couple


class IsAdminUserOrReadOnly(permissions.BasePermission):

    """
    Admin 유저가 아닐 경우, Read만 허용
    """

    def has_permission(self, request, view):
        print request.user
        print request.user.is_staff
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return False
