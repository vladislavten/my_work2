import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkwidgets import Calendar


def upload():
    general_start_command = False
    cmd_command = r"C:\CENTUMVP\program\BKHTrCSV.exe"
    if var_trace_l.get():
        cmd_command += " -l"
    if var_trace_t.get():
        if start_date.selection and end_date.selection:
            cmd_command += " -t"
            cmd_command += f' {start_date.selection.strftime("%m%d%H%M%Y")}'
            cmd_command += f' {end_date.selection.strftime("%m%d%H%M%Y")}'
            general_start_command = True
            print(start_date.selection)
        else:
            messagebox.showinfo('Ошибка', 'Заполните поля даты и время')
            general_start_command = False

    if trend_group.get():
        if len(trend_group.get()) == 4:
            if var_trace_l.get():
                cmd_command += f' {trend_group.get()}'
                general_start_command = True
            else:
                messagebox.showinfo('Ошибка', '"Не установлен флаг -l"')
                general_start_command = False
        else:
            messagebox.showinfo('Ошибка', 'Укажите 4 символа в поле "Группа трендов"')
            general_start_command = False
    else:
        general_start_command = False

    if general_start_command:
        subprocess.Popen(["cmd", "/c", cmd_command])
    else:
        messagebox.showinfo('Ошибка', 'Выгрузка не запущена, проверьте введенные данные')
    print(cmd_command)


root = tk.Tk()
root.title("Выгрузка трендов by Тен В.С.")
root.geometry('350x570')
root.resizable(False, False)

var_trace_l = tk.BooleanVar()
var_trace_l.set(True)
check_trace_l = tk.Checkbutton(root, text="Установить флаг -l", variable=var_trace_l)
check_trace_l.pack()

var_trace_t = tk.BooleanVar()
var_trace_t.set(True)
check_trace_t = tk.Checkbutton(root, text="Установить флаг -t", variable=var_trace_t)
check_trace_t.pack()

start_date_label = tk.Label(root, text="Начальная дата:")
start_date_label.pack()
start_date = Calendar(root)
start_date.pack(pady=5)

end_date_label = tk.Label(root, text="Конечная дата:")
end_date_label.pack()
end_date = Calendar(root)
end_date.pack(pady=5)

trend_group_label = tk.Label(root, text="Группа трендов:")
trend_group_label.pack()
trend_group = tk.Entry(root)
trend_group.pack(pady=5)

button_upload = tk.Button(root, text="ВЫГРУЗКА", command=upload)
button_upload.pack(pady=10)

root.mainloop()
