from rest_framework.permissions import BasePermission
from datetime import date

class IsOwner(BasePermission):
    message = "You're not the owner."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        else:
            return False
class IsValidd (BasePermission):
	message = "Sorry cannot modify/cancel."

	def has_object_permission(self, request, view, obj):
		if ((obj.date-date.today()).days)>3:
			return True
		else:
			return False
