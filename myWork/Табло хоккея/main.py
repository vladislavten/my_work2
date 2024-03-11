import tkinter as tk
import pickle

# Словарь для хранения данных
data_team = {}


# Функция для сохранения данных
# def save_data():
#     with open("data_team.pkl", "wb") as f:
#         pickle.dump(data_team, f)


def on_clear():
    global data_team
    data_team = {}
    with open("data_team.pkl", "wb") as f:
        pickle.dump(data_team, f)


# Функция для чтения данных
with open("data_team.pkl", "rb") as f:
    data_team = pickle.load(f)


def read_data():
    text_box.delete("1.0", "end")
    for key, value in data_team.items():
        text_box.insert("end", f"{key}: {value}\n")


# Функция для обработки нажатия кнопки
def on_click():
    global data_team
    key = entry_key.get()
    value = entry_value.get()
    data_team[key] = value
    with open("data_team.pkl", "wb") as f:
        pickle.dump(data_team, f)



# Создание окна
root = tk.Tk()
root.title("Сохранение данных в словарь")

# Создание виджетов
label_key = tk.Label(text="Ключ:")
entry_key = tk.Entry()

label_value = tk.Label(text="Значение:")
entry_value = tk.Entry()

button_save = tk.Button(text="Сохранить", command=on_click)
button_read = tk.Button(text="Читать", command=read_data)
button_clear = tk.Button(text="Стереть", command=on_clear)

text_box = tk.Text(height=10, width=30)

# Размещение виджетов
label_key.pack()
entry_key.pack()

label_value.pack()
entry_value.pack()

button_save.pack()
button_read.pack()
button_clear.pack()

text_box.pack()

# Загрузка данных при запуске программы
try:
    with open("data_team.pkl", "rb") as f:
        data_team = pickle.load(f)
except FileNotFoundError:
    pass

# Запуск цикла обработки событий
root.mainloop()

# Сохранение данных при закрытии окна
# save_data()
