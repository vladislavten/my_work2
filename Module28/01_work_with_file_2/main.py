import os


class File:
    """
    Контекст менеджер. При попытке открыть несуществующий файл,
    менеджер автоматически создаёт и открывает этот файл в
    режиме записи
    """
    def __init__(self, name: str, read_write: str) -> None:
        self.name = name
        self.read_write = read_write
        self.exists_flag = False

    def __enter__(self):
        if not os.path.exists(self.name):
            self.file = open(self.name, self.read_write, encoding='utf-8')
            self.exists_flag = True
            print('Файл создан. Данные записаны в файл: {}'.format(self.name))
            return self.file
        else:
            print('Файл существует')

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.exists_flag:
            self.file.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')
    test_error = 1 / 0
