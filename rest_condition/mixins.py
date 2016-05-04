__all__ = ('UpdatedPermissionChecksMixin',)

class UpdatedPermissionChecksMixin(object):
    """
    Updated permission checks mixin.
    """
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            has_perm = permission.has_permission(request, self)
            if not has_perm:
                message = has_perm.message \
                    if hasattr(has_perm, 'message') and has_perm.message \
                    else getattr(permission, 'message', None)
                self.permission_denied(
                    request, message=message
                )

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            has_perm = permission.has_object_permission(request, self, obj)
            if not has_perm:
                message = has_perm.message \
                    if hasattr(has_perm, 'message') and has_perm.message \
                    else getattr(permission, 'message', None)
                self.permission_denied(
                    request, message=message
                )
