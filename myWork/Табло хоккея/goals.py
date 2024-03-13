# import tkinter as tk
# from tkinter import simpledialog
# import pygame
# import os
#
# def play_video():
#     # Запрос пути к видеофайлу
#     video_path = 'D:\Python_Basic\myWork\Табло хоккея\win.mp4'
#
#     # Проверяем, что пользователь выбрал файл
#     if video_path:
#         # Запускаем проигрывание видео
#         pygame.mixer.init()
#         pygame.display.set_caption("Проигрывание видео")
#         screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)
#         pygame.mixer.quit()
#         clip = pygame.movie.Movie(video_path)
#         clip.set_display(screen, pygame.Rect(0, 0, 800, 600))
#         clip.play()
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Проигрывание видео")
#
# # Создаем кнопку для запуска проигрывания видео
# play_button = tk.Button(root, text="Выбрать видео и воспроизвести", command=play_video)
# play_button.pack(pady=20)
#
# # Запускаем основной цикл программы
# root.mainloop()

import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2
import os

def play_video():
    # Запрос пути к видеофайлу
    video_path = 'D:\Python_Basic\myWork\Табло хоккея\win.mp4'

    # Проверяем, что пользователь выбрал файл
    if video_path:
        # Проигрываем видео
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            messagebox.showerror("Ошибка", "Не удалось открыть видеофайл.")
            return

        # Определяем размеры экрана
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Создаем окно для видеоплеера на весь экран
        cv2.namedWindow("Видео", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Видео", screen_width, screen_height)

        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Видео", frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

def cancel_playback():
    cv2.destroyAllWindows()

# Создаем главное окно
root = tk.Tk()
root.title("Проигрывание видео")

# Создаем кнопку для запуска проигрывания видео
play_button = tk.Button(root, text="Выбрать видео и воспроизвести", command=play_video)
play_button.pack(pady=10)

# Создаем кнопку отмены
cancel_button = tk.Button(root, text="Отмена", command=cancel_playback)
cancel_button.pack(pady=5)

# Запускаем основной цикл программы
root.mainloop()
