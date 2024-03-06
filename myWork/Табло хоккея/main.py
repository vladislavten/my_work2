import tkinter as tk
from PIL import Image, ImageTk


def resize_image(image_path):
    image = Image.open(image_path)

    width, height = image.size

    # Вычисление нового размера изображения
    new_width = 400
    new_height = int(height * (new_width / width))

    resized_image = image.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)

def center_image(canvas, image):
    canvas.create_image(300, 300, anchor='center', image=image)

# Создание окна
root = tk.Tk()
root.title("Отображение изображения")

# Создание холста
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Путь к фотографии
photo_path = "photo_home/1.jpg"  # Замените на свой путь к фото

# Получение измененного изображения
image = resize_image(photo_path)

# Отображение изображения по центру холста
center_image(canvas, image)

root.mainloop()
