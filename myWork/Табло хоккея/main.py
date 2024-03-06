import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class PhotoViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer")
        self.root.attributes('-topmost', True)  # Устанавливаем флаг topmost для окна

        self.label = tk.Label(root, text="Введите номер игрока:")
        self.label.pack()

        self.player_number_entry = tk.Entry(root)
        self.player_number_entry.pack()

        self.show_photo_button = tk.Button(root, text="Показать фото", command=self.show_photo)
        self.show_photo_button.pack()

    def show_photo(self):
        player_number = self.player_number_entry.get()
        photo_path = f"photo/{player_number}.jpg"

        if os.path.exists(photo_path):
            photo = Image.open(photo_path)
            photo = photo.resize((300, 300))
            photo = ImageTk.PhotoImage(photo)

            self.photo_label = tk.Label(self.root, image=photo)
            self.photo_label.image = photo
            self.photo_label.pack()
        else:
            messagebox.showinfo("Ошибка", "Такое фото отсутствует")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoViewerApp(root)
    root.mainloop()
