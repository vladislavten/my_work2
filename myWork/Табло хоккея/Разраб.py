import tkinter as tk
from tkinter import messagebox

def show_info():
    # Создание нового окна с информацией
    info_window = tk.Toplevel()
    info_window.title("Информация")
    info_window.geometry("300x100")

    # Текст в новом окне
    label_info = tk.Label(info_window, text="Тен Владислав +77017107829", font=("Arial", 12))
    label_info.pack(expand=True)

# Создание основного окна
root = tk.Tk()
root.title("Главное окно")
root.geometry("300x100")

# Текст "Разработчик" в центре окна
label = tk.Label(root, text="Разработчик", font=("Arial", 16), fg="blue", cursor="hand2")
label.pack(expand=True)

# Связывание нажатия с функцией show_info
label.bind("<Button-1>", lambda e: show_info())

# Запуск основного цикла
root.mainloop()
