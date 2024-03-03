import os

# Получаем путь к папке, в которой лежит исполняемый файл
folder_path = os.path.dirname(os.path.abspath(__file__))

print("Путь к папке с исполняемым файлом:", folder_path)
