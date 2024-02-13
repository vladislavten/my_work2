import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

text = tk.Text(root)
text.pack()

# Настройка тега с прозрачным фоном
text.tag_configure("transparent", background="SystemButtonFace")

# Вставляем текст с использованием тега
text.insert("1.0", "Привет, мир!", "transparent")

# Устанавливаем альфа-канал цвета фона текста
text.configure(insertbackground='white')

root.mainloop()
