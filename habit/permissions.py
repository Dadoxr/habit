from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """
    Custom permission class to check if the user is the owner of the object or a staff member.
    """

    def has_permission(self, request, view):
        """
        Check if the user has permission to access the view.

        Args:
            request: The request object.
            view: The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """

        is_staff = request.user.is_staff
        is_owner = request.user == view.get_object().user

        return is_staff or is_owner
