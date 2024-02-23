import tkinter as tk
from tkinter import messagebox

def function1():
    print("Функция 1 запущена!")

def function2():
    print("Функция 2 запущена!")

def start_both_functions():
    function1()
    function2()
    messagebox.showinfo("Информация", "Обе функции были успешно выполнены!")

# Создание главного окна
root = tk.Tk()
root.title("Пример кнопки СТАРТ")

# Создание кнопки "СТАРТ"
start_button = tk.Button(root, text="СТАРТ", command=start_both_functions)
start_button.pack()

root.mainloop()