
import subprocess
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox


def upload():
    general_start_command = False
    cmd_command = f"C:\CENTUMVP\program\BKHTrCSV.exe"
    if var_trace_l.get():
        cmd_command += " -l"
        general_start_command = True
    if var_trace_t.get():
        if start_time_hour.get() and start_time_minutes.get() and end_time_hour.get() and end_time_minutes.get():
            cmd_command += " -t"
            cmd_command += f' {start_date.get_date().strftime("%m%d")}'
            cmd_command += f'{start_time_hour.get()}'
            cmd_command += f'{start_time_minutes.get()}'
            cmd_command += f'{start_date.get_date().strftime("%Y")}'

            cmd_command += f' {end_date.get_date().strftime("%m%d")}'
            cmd_command += f'{end_time_hour.get()}'
            cmd_command += f'{end_time_minutes.get()}'
            cmd_command += f'{end_date.get_date().strftime("%Y")}'
            general_start_command = True
        else:
            messagebox.showinfo('Ошибка', 'Заполните поля даты и время')
            general_start_command = False
    else:
        general_start_command = False

    if trend_group.get():
        if len(trend_group.get()) == 4:
            if var_trace_l.get():
                cmd_command += f' {trend_group.get()}'
                # general_start_command = True
            else:
                messagebox.showinfo('Ошибка', '"Не установлен флаг -l"')
                general_start_command = False
        else:
            messagebox.showinfo('Ошибка', 'Укажите 4 символа в поле "Группа трендов"')
            general_start_command = False

    if general_start_command:
        subprocess.Popen(["cmd", "/c", cmd_command], )
    else:
        messagebox.showinfo('Ошибка', 'Выгрузка не запущена, проверьте введенные данные"')
        general_start_command = False
    print(cmd_command)


root = tk.Tk()
root.title("Выгрузка трендов by Тен В.С.")
root.geometry('350x450')
root.resizable(False, False)

var_trace_l = tk.BooleanVar()
var_trace_l.set('1')
check_trace_l = tk.Checkbutton(root, text="Установить флаг -l", variable=var_trace_l).pack()

var_trace_t = tk.BooleanVar()
var_trace_t.set('1')
check_trace_t = tk.Checkbutton(root, text="Установить флаг -t", variable=var_trace_t).pack()

start_date_label = tk.Label(root, text="Начальная дата:")
start_date_label.pack()
start_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date.pack(pady=5)

start_time_label = tk.Label(root, text="Начальное время:")
start_time_label.pack()

start_time_hour = ttk.Combobox(root, values=[str(num).zfill(2) for num in range(24)])
start_time_hour.set("00")
start_time_hour.pack(pady=5)

start_time_minutes = ttk.Combobox(root, values=[str(num).zfill(2) for num in range(60)])
start_time_minutes.set('00')
start_time_minutes.pack(pady=5)

end_date_label = tk.Label(root, text="Конечная дата:")
end_date_label.pack()
end_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date.pack(pady=5)

end_time_label = tk.Label(root, text="Конечное время:")
end_time_label.pack()
end_time_hour = ttk.Combobox(root, values=[str(num).zfill(2) for num in range(24)])
end_time_hour.set('00')
end_time_hour.pack(pady=5)

end_time_minutes = ttk.Combobox(root, values=[str(num).zfill(2) for num in range(60)])
end_time_minutes.set('00')
end_time_minutes.pack(pady=5)

trend_group_label = tk.Label(root, text="Группа трендов:")
trend_group_label.pack()
trend_group = tk.Entry(root)
trend_group.pack(pady=5)

button_upload = tk.Button(root, text="ВЫГРУЗКА", command=upload)
button_upload.pack(pady=10)

root.mainloop()
