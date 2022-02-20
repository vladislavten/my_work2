from typing import Callable
import time


def how_are_you(func: Callable, *args, **kwargs) -> Callable:
    """
    Декоратор. Задает надоедливый вопрос "Как дела?"
    """
    print('Как дела? ')
    print('Подожди 3 секунды')
    time.sleep(3)
    return func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

