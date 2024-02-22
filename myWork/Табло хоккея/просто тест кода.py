import tkinter as tk


def main():
    # Создание главного окна
    root = tk.Tk()
    root.title("Пример с Tkinter")

    # Установка размеров окна
    root.geometry("500x500")

    # Создание рамки
    frame = tk.Frame(root, width=100, height=100, bg="red", highlightthickness=8, highlightbackground="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Создание надписи внутри рамки
    label = tk.Label(frame, text="РАМКА", fg="white", bg="red")
    label.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    main()
