

class Calc:
    def __init__(self, number: int) -> None:
        self.counter = 0
        self.num = number
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.num != self.counter:
            self.counter += 1
            self.result = self.counter ** 2
            return self.result
        else:
            raise StopIteration()


def square(number: int) -> int:
    count = 1
    for _ in range(number):
        result = count ** 2
        yield result
        count += 1


enter_number = int(input('Введите число: '))
my_iter = Calc(enter_number)
print('Класс итератор:')
for num in my_iter:
    print(num, end=' ')

square_iter = square(enter_number)
print('\n\nФункция генератор:')
for i_value in square_iter:
    print(i_value, end=' ')

print('\n\nГенерааторное выражение:')
square_gen = (gen ** 2 for gen in range(1, enter_number + 1))
for i_num in square_gen:
    print(i_num, end=' ')