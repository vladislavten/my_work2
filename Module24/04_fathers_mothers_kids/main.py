
class Parent:
    name_parent = 'Уля'
    age_parent = 34
    daughter_1 = 'Земфира'
    daughter_2 = 'Белла'

    def info_parent(self):
        print('\nИнформация родителя:')
        print('Имя:', self.name_parent)
        print('Возраст:', self.age_parent)
        print('Дети: {}, {}'.format(self.daughter_1, self.daughter_2))

    def keep_calm(self):
        print('Какого ребенка хотите успокоить?')
        choice_element = int(input('"1"-Земфира, "2"-Белла \nВвод'))
        if choice_element == 1:
            zemfira.calmness = True
            print('Состояние спокойствия', zemfira.name, '=', calm_dct[zemfira.calmness])
        elif choice_element == 2:
            bella.calmness = True
            print('Состояние спокойствия', bella.name, '=', calm_dct[bella.calmness])
        else:
            print('Ошибка ввода!')

    def feed_child(self):
        print('Какого ребенка хотите покормить  ?')
        choice_element = input('"1"-Земфира, "2"-Белла \nВвод ')
        if choice_element == '1':
            zemfira.feed = True
            print('Состояние голода', zemfira.name, '=', feed_dct[zemfira.feed])
        elif choice_element == '2':
            bella.feed = True
            print('Состояние голода', bella.name, '=', feed_dct[bella.feed])
        else:
            print('Ошибка ввода!')


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calmness = False
        self.feed = False

    def feed(self):
        self.feed = True

    def calm(self):
        self.calmness = True

# TODO ключем не может быть булева переменная
feed_dct = {True: 'Накормлена', False: 'Голодная'}
calm_dct = {True: 'Спокойна', False: 'Не спокойна'}

mother = Parent()
zemfira = Child('Земфира', 11)
bella = Child('Белла', 2)
while True:
    print('\nВыберите пункт:\n'
          '1 = Информация о себе\n'
          '2 = Успокоить ребёнка\n'
          '3 = Покормить ребёнка')
    choice = input('Ввод: ')
    if choice == '1':
        mother.info_parent()
    elif choice == '2':
        mother.keep_calm()
    elif choice == '3':
        mother.feed_child()
    else:
        print('Ошибка ввода!')

# TODO применить рекомендации данные ранее
