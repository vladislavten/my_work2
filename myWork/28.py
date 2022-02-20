# 28.2 Множественное наследование: MRO

# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих:
# разведывательного дрона и военного робота.
#
# Разведывательный дрон просто летает в поиске противника.
# При команде operate он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
#
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение о защите военного
# объекта с воздуха с помощью этого оружия.
#
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и «Может летать»
# должны быть вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот».
# Объект, который умеет летать, дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать,
# летать и приземляться.

class Robot:
    """Базовая модель класса Робот"""
    def __init__(self, model: str):
        self.model = model

    def say(self):
        print(f'Я робот {self.model}')


class Fly:
    @staticmethod
    def can_fly():
        print('Я полетел')


class Fly_robot(Robot, Fly):
    def __init__(self, model: str, height: bool, speed: int):
        super().__init__(model)
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height = True
        print('Я взлетел. Мой статус: {}'.format(self.height))

    def fly_down(self):
        self.height = False
        print('Я приземлился. Мой статус: {}'.format(self.height))


basic_robot = Robot('Xr34')
basic_robot.say()

warrior_robot = Fly_robot('XC35', False, 120)
warrior_robot.say()
warrior_robot.can_fly()
warrior_robot.fly_up()
warrior_robot.fly_down()



