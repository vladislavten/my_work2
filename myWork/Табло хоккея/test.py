import tkinter as tk

# Создаем словарь с данными об игроках
data_team = {'23': 'Тен Владислав', '22': 'Тен Ульяна', '30': 'Роман Калмыков'}
def show_players():
    # Очищаем текстовое поле перед добавлением новых данных
    text_box.delete(1.0, tk.END)

    # Выводим игроков в текстовое поле
    for number, name in data_team.items():
        text_box.insert(tk.END, f"номер: {number}  Имя/Фамилия: {name}\n")
        text_box.place(x=1, y =100)


# Создаем графический интерфейс
root = tk.Tk()
root.title("Игроки команды")
root.geometry('500x500')

# Создаем кнопку "Показать игроков"
show_button = tk.Button(root, text="Показать игроков", command=show_players)
show_button.pack(pady=10)

# Создаем текстовое поле для вывода игроков
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

root.mainloop()
