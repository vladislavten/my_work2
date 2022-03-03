user_permissions = ['admin']


def check_permission(permission):
    def wrapper_permission(func):
        def wrapped_check():
            try:
                if permission not in user_permissions:
                    raise PermissionError
            except PermissionError:
                print("PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment", )
            return func()
        return wrapped_check
    return wrapper_permission


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

