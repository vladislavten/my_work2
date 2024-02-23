import pyautogui

# Получить список всех подключенных мониторов
monitors = pyautogui.getDisplays()

# Если есть второй монитор, получить его размеры
if len(monitors) >= 2:
    second_monitor = monitors[1]
    width = second_monitor.width
    height = second_monitor.height

    # Вывести информацию о размерах второго монитора
    print(f"Ширина второго монитора: {width}")
    print(f"Высота второго монитора: {height}")
else:
    print("Второй монитор не найден.")
