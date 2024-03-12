import tkinter as tk
from tkinter import messagebox
import configparser

# Создаем словарь с данными об игроках
data_team = {'23': 'Тен Владислав', '22': 'Тен Ульяна', '30': 'Роман Калмыков'}


def show_players():
    print('OK')


def check_license():
    try:
        # Загрузка файла конфигурации
        config = configparser.ConfigParser()
        config.read('config.fhp')
        license_key = config.get('License', 'key')
        return license_key == 'qwerty123'
    except configparser.NoSectionError:
        return False
    except configparser.NoOptionError:
        return False


def save_license(key):
    # Создание файла конфигурации и сохранение ключа
    config = configparser.ConfigParser()
    config['License'] = {'key': key}
    with open('config.fhp', 'w') as config_file:
        config.write(config_file)


def enter_license_key():
    key = entry_license_key.get()
    if key == 'qwerty123':
        save_license(key)
        root_license.destroy()
        show_players()
    else:
        messagebox.showerror("Ошибка", "Неверный лицензионный ключ")


# Проверка наличия лицензионного ключа при запуске программы
if not check_license():
    root_license = tk.Tk()
    root_license.title("Введите лицензионный ключ")

    label_license_key = tk.Label(root_license, text="Введите лицензионный ключ:")
    label_license_key.pack(pady=10)

    entry_license_key = tk.Entry(root_license, show="*")
    entry_license_key.pack(pady=5)

    button_submit = tk.Button(root_license, text="Ввести ключ", command=enter_license_key)
    button_submit.pack(pady=5)

    root_license.mainloop()
else:
    # Если лицензионный ключ верный, сразу показываем игроков
    show_players()


