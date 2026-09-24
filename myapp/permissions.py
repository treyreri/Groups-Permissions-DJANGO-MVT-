from functools import wraps #wraps нужен для того чтобы наш декоратор нормально сохранял информацию об исъодной функции
from django.core.exceptions import PermissionDenied

def permission_required(permission): #эта функция принимает название permission например permission_required('myapp.add_course') permission = 'myapp.add_course'
    def decorator(view_func): #view_func - это наша обычная функция например та поднижняя def course_create(request):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if not request.user.has_perm(permission):
                raise PermissionDenied #если у пользователя нет права мы сделаем это, и DJANGO вернет 403 Forbidden

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator