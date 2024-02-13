
















from colorama import init, Fore

# Инициализация colorama
init()

# Проверка значения переменной a
a = input("Введите значение переменной a: ")

if a == '1':
    # Вывод "Все правильно" зеленым цветом
    print(Fore.GREEN + "Все правильно")
else:
    # Вывод "ОШИБКА" красным цветом
    print(Fore.RED + "ОШИБКА")