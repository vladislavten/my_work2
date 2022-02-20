import functools
from typing import Callable


def debug(function: Callable) -> Callable:
    """
    Декоратор debug, который при каждом вызове декорируемой функции выводит её имя
    (вместе со всеми передаваемыми аргументами) и затем какое значение она возвращает.
    И после этого выводится результат её выполнения
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("Вызывается {}({})".format(function.__name__,
                                         ", ".join(
                                             list(f"\"{arg}\""
                                                  if isinstance(arg, str) else
                                                  str(arg) for arg in args)
                                             +
                                             list(f"{key}=\"{value}\""
                                                  if isinstance(value, str) else
                                                  f"{key}={value}" for key, value in kwargs.items())
                                         )
                                         ))
        result = function(*args, **kwargs)
        print("'{}' вернула значение '{}'".format(
            function.__name__, result
        ))
        print(result)
        return result

    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
