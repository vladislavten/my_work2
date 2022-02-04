class MyDict:
    __my_dict = {1: 'asd', 2: 'qwe', 3: 'zxc'}

    def get_my_dict(self, value):
        if value in self.__my_dict:
            return 'Значение: {}'.format(self.__my_dict[value])
        else:
            return 0


find = MyDict()
print(find.get_my_dict(3))

find_2 = MyDict()
print(find_2.get_my_dict(5))
