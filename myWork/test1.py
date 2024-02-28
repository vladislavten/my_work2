import tkinter as tk
from screeninfo import get_monitors


def open_window_on_secondary_monitor():
    # Получаем список мониторов
    monitors = get_monitors()
    print(monitors)

    if len(monitors) < 2:
        print("Второй монитор не обнаружен.")
        return

    # Выбираем второй монитор (индекс 1)
    secondary_monitor = monitors[1]

    # Создаем окно Tkinter
    root = tk.Tk()

    #убираем рамки окна
    root.overrideredirect(True)

    # Устанавливаем геометрию окна для второго монитора в полноэкранном режиме без рамок
    root.geometry(f"{secondary_monitor.width}x{secondary_monitor.height}+{secondary_monitor.x}+{secondary_monitor.y}")
    # root.attributes('-fullscreen', True)

    # Добавляем информацию
    label = tk.Label(root, text="Информация", font=("Helvetica", 36))
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    open_window_on_secondary_monitor()
