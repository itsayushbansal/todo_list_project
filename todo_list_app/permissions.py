def has_object_permission(request, obj):
    """
    Return `True` if permission is granted, `False` otherwise.
    """
    return request.user == obj.user
