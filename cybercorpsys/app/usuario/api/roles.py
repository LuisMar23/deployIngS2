from rest_framework_roles.roles import is_user, is_admin, is_anon, is_staff

def is_asesor(request, view):
    request.user.usertype = 'asesor'
    return is_user(request, view) and request.user.usertype

def is_contador(request, view):
    request.user.usertype = 'asesor'
    return is_asesor(request, view) and request.user.usertype


ROLES = {
    'admin':is_admin,
    'user':is_user,
    'anon':is_anon,
    'staff':is_staff,
    'asesor':is_asesor,
    'contador':is_contador
}