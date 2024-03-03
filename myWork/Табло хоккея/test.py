import os.path
import tkinter
import tkinter as tk
from PIL import Image, ImageTk
import time

def show_photo():
    if os.path.exists(f'{os.path.dirname(__file__)}\\photo\\{number_entry.get()}.jpg'):
        photo_window = tk.Toplevel(root)
        photo_window.title("Фото")
        photo_window.attributes('-fullscreen', True)
        photo_window.configure(background='black')

        # Загрузка изображения
        image_path = f"photo\\{number_entry.get()}.jpg"
        image = Image.open(image_path)
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)


        print(number_entry.get())
        name = tk.Label(text='ШАЙБУ ЗАБИЛ')

        # Отображение изображения на метке
        photo_label = tk.Label(photo_window, image=photo)
        photo_label.image = photo  # сохраняем ссылку на изображение, чтобы избежать сборщика мусора
        photo_label.place(relx=0.25, rely=0.2, anchor='center')

        # Закрытие окна через 5 секунд
        photo_window.after(3000, photo_window.destroy)

    else:
        photo_window = tk.Toplevel(root)
        photo_window.title("Фото")
        photo_window.attributes('-fullscreen', True)
        photo_window.configure(background='black')
        no_name = tk.Label(photo_window, text=f'Гол забил номер: {number_entry.get()} ', font=('Helvetica', 100), bg='black', fg='red')
        no_name.place(relx=0.5, rely=0.5, anchor='center')

        photo_window.after(3000, photo_window.destroy)
        print('NO')

root = tk.Tk()
root.title("Гол забил")
root.geometry('200x200')

number_entry = tk.Entry(root)
number_entry.pack()

exit_button = tk.Button(root, text="Гол забил", command=show_photo)
exit_button.pack()

root.mainloop()
