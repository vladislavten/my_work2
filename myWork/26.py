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


# import turtle
#
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
# color = ('green', 'blue', 'yellow', 'red', 'cyan', 'white', 'pink', 'brown')
# for i in range(300):
#     t.color(color[i%8])
#     t.left(560)
#     t.forward(i*5)
#     t.rt(2)


# 26.4 Реализация итераторов

# Задача 1. Бесконечный итератор

#
# class Ya:
#     def __init__(self):
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         return self.counter
#
# my_iter = Ya()
#
# for i_elem in my_iter:
#     print(i_elem)

#
# import time, random, webbrowser
#
# for i in range(5):
#     a = random.choice(['ya.ru', 'mail.ru'])
#     webbrowser.open('http://{}'.format(a))
#     time.sleep(3)


#
# import random
# import time
# start_time = time.time()
#
#
# class Calc:
#     def __init__(self, num):
#         self.counter = 0
#         self.result = 0
#         self.num = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.result < self.num:
#             self.counter += random.uniform(0, 1)
#             self.result += 1
#             return round(self.counter, 2)
#         else:
#             raise StopIteration()
#
#
# number = int(input('Введите число: '))
# my_iter = Calc(number)
#
# for num in my_iter:
#     print(num)
#
# print("--- %g seconds ---" % (time.time() - start_time))