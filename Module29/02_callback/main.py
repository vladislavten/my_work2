app = {}


def callback(route):
    def wrapper(func):
        app[route] = func

        def wrapped():
            ret = func()
            return ret

        return wrapped

    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


print('> старт')
route = app.get('//')
if route:
    resp = route()
    print('ответ:', resp)

print('>  конец')
