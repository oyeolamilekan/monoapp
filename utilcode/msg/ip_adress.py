"""
this is utility function is used to get client ip address
"""
def get_client_ip(request):
    """
    Get the user client ip address, and remote the information
    Arguments:
        request {request object} -- Get request info needed to get ip address
    Returns:
        string -- returns a string of the user ip address
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        i_p = x_forwarded_for.split(",")[0]
    else:
        i_p = request.META.get("REMOTE_ADDR")
    return i_p
