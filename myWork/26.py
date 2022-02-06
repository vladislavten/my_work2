# 26.2 Итераторы

# Задача 1. Свой for (ну почти)

# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая
# эмулирует работу цикла for с помощью цикла while и проходит во всем элементам итерируемого
# объекта. Не забудьте про исключение «конца итерации».

# def my_iter(i):
#     iterator = iter(i)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break
#
# asd = [10, 20, 30, 40]
#
# my_iter(asd)

#
# import turtle
#
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
# color = ('green', 'blue', 'yellow', 'red', 'cyan')
# for i in range(150):
#     t.color(color[i%5])
#     t.left(150)
#     t.forward(i*2)
#     t.rt(72)


# 26.4 Реализация итераторов

# Задача 1. Бесконечный итератор


class Ya:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        self

    def __next__(self):
        self.counter += 1
        return self.counter

my_iter = Ya()

for i_elem in my_iter:
    print(i_elem)



