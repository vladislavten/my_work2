import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    """
    Декоратор. Вывод название фукнции и ее документацию.
    Если в декорируемой функции есть ошибки, логирует их в файл function_errors.log
    """
    try:
        func()
        print('Имя функции:', func.__name__)
        print('Документация функции', func.__doc__)
    except NameError:
        print('Обнаружена ошибка в функции, и записана в файл function_errors.log')
        with open('function_errors.log', 'a', encoding='utf-8') as logs:
            logs.write('Имя функции - {}. Ошибка - NameError. Время ошибки: {}\n'
                       .format(func.__name__, datetime.datetime.now()))
    except:
        print('Обнаружена ошибка в функции, и записана в файл function_errors.log')
        with open('function_errors.log', 'a') as logs:
            logs.write('Имя функции - {}. Ошибка - неизвестна\n'.format(func.__name__))


@logging
def test() -> None:
    """
    Обычная фукция без ошибок, которая что-то выводит на экран.
    """
    print('<Тут что-то происходит...>')


@logging
def test2() -> None:
    """
    Обычная фукция c ошибокой NameError, которая что-то выводит на экран.
    """
    print(aaa)


@logging
def test3() -> None:
    """
    Обычная фукция c ошибокой NameError, которая что-то выводит на экран.
    """
    print('Test {}'.format(asd))


first_def = test
second_def = test2
third_def = test3
