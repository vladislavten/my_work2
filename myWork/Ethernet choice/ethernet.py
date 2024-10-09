import tkinter as tk
import subprocess


def off_anpz_ethernet():
    # Выполняем команду для отключения интерфейса, скрывая окно
    command1 = "netsh interface set interface anpz admin=disable"
    command2 = "netsh interface set interface wifi admin=enable"
    subprocess.run(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    button1.config(state=tk.DISABLED)
    button2.config(state=tk.NORMAL)
    status_label.config(text="Сейчас подключен Beeline")


def off_wifi():
    # Выполняем команду для отключения интерфейса, скрывая окно
    command1 = "netsh interface set interface anpz admin=enable"
    command2 = "netsh interface set interface wifi admin=disable"
    subprocess.run(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    button2.config(state=tk.DISABLED)
    button1.config(state=tk.NORMAL)
    status_label.config(text="Сейчас подключен АНПЗ")


master = tk.Tk()
master.title("Переключение сетевых карт")
master.geometry('200x150')
master.resizable(False, False)
master['bg'] = 'lightblue'

button1 = tk.Button(master, text="Включить Beeline", command=off_anpz_ethernet)
button1.pack(anchor='center', pady=(20, 0))

button2 = tk.Button(master, text="Включить АНПЗ", command=off_wifi)
button2.pack(anchor='center', pady=(20, 0))

status_label = tk.Label(master, text="Сейчас ничего не подключено", bg='lightblue')
status_label.pack(anchor='center', pady=(20, 0))

master.mainloop()
