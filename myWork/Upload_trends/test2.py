import tkinter as tk
from calendar_widget import Calendar


def upload():
    # cmd_command += " -t"
    # cmd_command += f' {start_date.selection.strftime("%m%d%H%M%Y")}'
    # cmd_command += f' {end_date.selection.strftime("%m%d%H%M%Y")}'

    print(end_date.getdate())


root = tk.Tk()
root.title("Выгрузка трендов by Тен В.С.")
root.geometry('350x570')
# root.resizable(False, False)

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
# start_date.pack(pady=5)

end_date_label = tk.Label(root, text="Конечная дата:")
end_date_label.pack()
end_date = Calendar(root)
# end_date.pack(pady=5)

trend_group_label = tk.Label(root, text="Группа трендов:")
trend_group_label.pack()
trend_group = tk.Entry(root)
trend_group.pack(pady=5)

button_upload = tk.Button(root, text="ВЫГРУЗКА", command=upload)
button_upload.pack(pady=10)

root.mainloop()
