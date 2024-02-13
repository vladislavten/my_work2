import tkinter as tk
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Управление Таймером")
        self.master.geometry("500x500")

        self.timer_window = tk.Toplevel(master)
        self.timer_window.title("Таймер")
        self.timer_window.geometry("1024x768")
        self.timer_window['bg'] = 'black'
        # self.timer_window.withdraw()

        self.timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 100), bg="black", fg="red")
        self.timer_label.pack(expand=True)
        self.timer_label.place(relx=0.5, rely=0.355, anchor="center")

        #Название команд игроков
        self.team1 = tk.Label(self.timer_window, text="БЕЙБАРЫС", font=("Helvetica", 40), bg="black", fg="white")
        self.team1.place(relx=0.2, rely=0.1, anchor="center")
        self.team2 = tk.Label(self.timer_window, text="АРЛАН", font=("Helvetica", 40), bg="black", fg="white")
        self.team2.place(relx=0.8, rely=0.1, anchor="center")

        #Текст ВРЕМЯ по центру
        self.time_text_label = tk.Label(self.timer_window, text="ТАЙМЕР", font=("Helvetica", 30), bg="black", fg="white")
        self.time_text_label.place(relx=0.5, rely=0.25, anchor="center")

        # Текст ПЕРИОД по центру
        self.time_text_label = tk.Label(self.timer_window, text="ПЕРИОД", font=("Helvetica", 25), bg="black", fg="white")
        self.time_text_label.place(relx=0.5, rely=0.55, anchor="center")

        self.timer_running = False
        self.time_remaining = 20 * 60  # 20 минут в секундах
        self.start_time = 0
        self.paused_time = 0

        #Создаем кнопки
        self.button = tk.Button(master, text="Старт", command=self.toggle_timer)
        self.button.pack()

        self.reset_button = tk.Button(master, text="Начать сначала", command=self.reset_timer)
        self.reset_button.pack()

        self.goal_home_var = tk.IntVar(value=0)

        #Счет команд
        self.goal_home_label = tk.Label(self.timer_window, textvariable=self.goal_home_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_home_label.place(relx=0.2, rely=0.3, anchor="center")

        self.goal_away_var = tk.IntVar(value=0)
        self.goal_away_label = tk.Label(self.timer_window, textvariable=self.goal_away_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_away_label.place(relx=0.8, rely=0.3, anchor="center")

        self.period_var = tk.IntVar(value=1)
        self.period_var_label = tk.Label(self.timer_window, textvariable=self.period_var, font=("DS-Digital", 100), bg="black", fg="green")
        self.period_var_label.place(relx=0.5, rely=0.68, anchor="center")

        self.goal_home_increase_button = tk.Button(master, text="+ Гол хозяева", command=self.goal_home_increase)
        self.goal_home_increase_button.pack()

        self.goal_home_decrease_button = tk.Button(master, text="- Гол хозяева", command=self.goal_home_decrease)
        self.goal_home_decrease_button.pack()

        self.goal_away_increase_button = tk.Button(master, text="+ Гол гости", command=self.goal_away_increase)
        self.goal_away_increase_button.pack()

        self.goal_away_decrease_button = tk.Button(master, text="- Гол гости", command=self.goal_away_decrease)
        self.goal_away_decrease_button.pack()

        self.add_minute_button = tk.Button(master, text="+ Минута", command=self.add_minute)
        self.add_minute_button.pack()

        self.subtract_minute_button = tk.Button(master, text="- Минута", command=self.subtract_minute)
        self.subtract_minute_button.pack()

        self.add_second_button = tk.Button(master, text="+ Секунда", command=self.add_second)
        self.add_second_button.pack()

        self.subtract_second_button = tk.Button(master, text="- Секунда", command=self.subtract_second)
        self.subtract_second_button.pack()

        self.period_increase_button = tk.Button(master, text="+ Период", command=self.period_increase)
        self.period_increase_button.pack()

        self.goal_home_decrease_button = tk.Button(master, text="- Период", command=self.period_decrease)
        self.goal_home_decrease_button.pack()

        self.fullscreen_button = tk.Button(master, text="Во весь экран", command=self.fullscreen_timer)
        self.fullscreen_button.pack(side=tk.RIGHT)

        self.fullscreen_state = False

        self.master.bind("<space>", self.toggle_timer_space)
        self.update_timer()

    def toggle_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.button.config(text="Старт")
            self.paused_time = time.time() - self.start_time
        else:
            if self.time_remaining == 0:  # если время истекло, начинаем отсчет сначала
                self.time_remaining = 20 * 60
            self.timer_running = True
            self.button.config(text="Стоп")
            self.start_time = time.time() - (20 * 60 - self.time_remaining)  # учитываем добавленные секунды или минуты
            self.update_timer()

    def toggle_timer_space(self, event):
        self.toggle_timer()

    def reset_timer(self):
        self.timer_running = False
        self.button.config(text="Старт")
        self.time_remaining = 20 * 60
        self.timer_label.config(text=self.format_time(self.time_remaining))
        self.start_time = 0
        self.paused_time = 0

    def goal_home_increase(self):
        if not self.timer_running:
            self.goal_home_var.set(self.goal_home_var.get() + 1)

    def goal_home_decrease(self):
        if not self.timer_running:
            self.goal_home_var.set(max(0, self.goal_home_var.get() - 1))

    def period_increase(self):
        if not self.timer_running:
            self.period_var.set(self.period_var.get() + 1)

    def period_decrease(self):
        if not self.timer_running:
            self.period_var.set(max(1, self.period_var.get() - 1))

    def goal_away_increase(self):
        if not self.timer_running:
            self.goal_away_var.set(self.goal_away_var.get() + 1)

    def goal_away_decrease(self):
        if not self.timer_running:
            self.goal_away_var.set(max(0, self.goal_away_var.get() - 1))

    def add_minute(self):
        if not self.timer_running:
            self.time_remaining += 60
            self.timer_label.config(text=self.format_time(self.time_remaining))

    def subtract_minute(self):
        if not self.timer_running:
            self.time_remaining = max(0, self.time_remaining - 60)
            self.timer_label.config(text=self.format_time(self.time_remaining))

    def add_second(self):
        if not self.timer_running:
            self.time_remaining += 1
            self.timer_label.config(text=self.format_time(self.time_remaining))

    def subtract_second(self):
        if not self.timer_running:
            self.time_remaining = max(0, self.time_remaining - 1)
            self.timer_label.config(text=self.format_time(self.time_remaining))

    def fullscreen_timer(self):
        if not self.fullscreen_state:
            self.timer_window.deiconify()
            self.timer_window.attributes("-fullscreen", True)
            self.fullscreen_state = True

        else:
            self.timer_window.attributes("-fullscreen", False)
            self.fullscreen_state = False
            self.timer_window.withdraw()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.time_remaining = max(0, 20 * 60 - elapsed_time)
            self.timer_label.config(text=self.format_time(self.time_remaining))
            if self.time_remaining > 0:
                self.timer_window.after(1000, self.update_timer)
            else:
                self.timer_running = False
                self.button.config(text="Старт")
        else:
            self.timer_label.config(text=self.format_time(self.time_remaining))

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
