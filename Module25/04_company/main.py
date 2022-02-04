class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age, salary=13000):
        super().__init__(name, surname, age)
        self.salary_sum = salary

    def salary(self):
        print('Зарплата менеджера {} {}: {}'.format(self.get_name(), self.get_surname(), self.salary_sum))


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.salary_sum = 5000 + (volume_of_sales / 100 * 5)

    def salary(self):
        print('Зарплата агента {} {}: {}'.format(self.get_name(), self.get_surname(), self.salary_sum))


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.salary_sum = 100 * hours

    def salary(self):
        print('Зарплата рабочего {} {}: {}'.format(self.get_name(), self.get_surname(), self.salary_sum))


manager_1 = Manager('Вася', 'Пупкин', 30)
manager_1.salary()
manager_2 = Manager('Миша', 'Горохов', 32)
manager_2.salary()
manager_3 = Manager('Алена', 'Даст', 35)
manager_3.salary()
agent_1 = Agent('Настя', 'Ивлеева', 27, 50000)
agent_1.salary()
agent_2 = Agent('Антон', 'Птушкин', 26, 75000)
agent_2.salary()
agent_3 = Agent('Филипп', 'Уиркоров', 59, 100000)
agent_3.salary()
worker_1 = Worker('Пашка', 'Петров', 26, 160)
worker_1.salary()
worker_2 = Worker('Ленка', 'Осипова', 29, 120)
worker_2.salary()
worker_3 = Worker('Гришка', 'Ямщиков', 41, 240)
worker_3.salary()
