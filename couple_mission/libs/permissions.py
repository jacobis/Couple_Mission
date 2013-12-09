from rest_framework import permissions

from couple_mission.apps.couple.controller import CoupleController


class IsOwnerOrCoupleOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        is_owner = bool(obj.user == request.user)
        is_couple = bool(CoupleController.get_couple(request.user))

        print is_owner
        print is_couple

        return is_owner or is_couple
