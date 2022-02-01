# TODO здесь писать код
class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary_sum = 13000

    def salary(self):
        print(self.salary_sum)


test = Manager('имя', 'фамилия', 30)
test.salary()
