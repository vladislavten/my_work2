import tkinter as tk
from datetime import datetime, timedelta

# Функция для переключения в полноэкранный режим
def fullscreen():
  # Переводим новое окно в полноэкранный режим
  new_window.deiconify()
  new_window.attributes('-fullscreen', True)
  new_window['bg'] = 'black'

# Функция для выхода из полноэкранного режима
def exit_fullscreen():
  # Проверяем, находится ли новое окно в полноэкранном режиме
  if new_window.attributes('-fullscreen'):
    # Выходим из полноэкранного режима
    # new_window.withdraw()
    new_window.attributes('-fullscreen', False)

def Hi():
  print('Hello dude!')



# Создаем корневой элемент окна
root = tk.Tk()
root.title('Бей-бей-Бейбарыс')

root['bg'] = 'black'

# Задаем размер окна
root.geometry('500x500')

# Создаем новое окно
new_window = tk.Toplevel(root)
test = tk.Toplevel(root)
test.geometry('500x500')
# new_window.withdraw()
new_window.geometry('300x300')
new_window['bg'] = 'black'

#Создаем лейбл
a = 0
time_text_label = tk.Label(test, text=a, font=("Helvetica", 35))
time_text_label.place(relx=0.5, rely=0.1, anchor="center")

# Создаем кнопки
button = tk.Button(root, text="Перейти в полноэкранный режим", command=fullscreen, bg="red", fg="white")
button_exit = tk.Button(root, text="Выйти из полноэкранного режима", command=exit_fullscreen, bg="red", fg="white")
button_test2 = tk.Button(root, text='+1', command=a+1)
button_test = tk.Button(new_window, text='TECT', command=Hi)
start_timer = tk.Button(root, text='Старт таймера')

# Размещаем кнопки
button.pack(expand=True)
button_exit.pack(expand=True)
button_test.pack(expand=True)
button_test2.pack()


# Обрабатываем нажатие клавиши ESC
root.bind("<Escape>", lambda event: exit_fullscreen())
new_window.bind("<Escape>", lambda event: exit_fullscreen())

# Запускаем главный цикл окна
root.mainloop()
