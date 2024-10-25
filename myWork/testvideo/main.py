import cv2
import tkinter as tk
from tkinter import Toplevel, Label
from PIL import Image, ImageTk

def play_video():
    # Создаем полноэкранное окно для видео
    video_window = Toplevel(root)
    video_window.title("Видеопроигрыватель")
    video_window.attributes("-fullscreen", True)  # Полноэкранный режим
    video_window.configure(bg="black")  # Черный фон

    # Текст "ГОЛ ЗАБИЛ" над видео с белым цветом
    label_text = Label(video_window, text="ГОЛ ЗАБИЛ", font=("Arial", 24), fg="white", bg="black")
    label_text.pack(pady=20)

    # Загружаем видео
    cap = cv2.VideoCapture("fola.mp4")
    video_label = Label(video_window, bg="black")  # Черный фон для метки с видео
    video_label.pack(pady=20)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Изменяем размер кадра до 400x400
            frame = cv2.resize(frame, (400, 400))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.after(10, update_frame)
        else:
            cap.release()
            video_window.destroy()

    update_frame()

# Главное окно
root = tk.Tk()
root.title("Футбольная игра")

# Кнопка "ГОЛ ЗАБИЛ"
goal_button = tk.Button(root, text="ГОЛ ЗАБИЛ", font=("Arial", 20), command=play_video)
goal_button.pack(pady=50)

root.mainloop()
