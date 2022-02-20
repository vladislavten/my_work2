from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, который считает количество вызова функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def hello():
    print('Hello world')


hello()
hello()
hello()

print('Функция запускалась: {} раз(а)'.format(hello.count))
