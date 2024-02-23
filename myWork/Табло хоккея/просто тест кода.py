import tkinter as tk
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Управление Таймером")
        self.master.geometry("600x600")



        # Добавляем поля ввода для имен команд и кнопку "Сохранить команды"
        self.team1_name_entry = tk.Entry(master)
        self.team1_name_entry.pack()
        self.team2_name_entry = tk.Entry(master)
        self.team2_name_entry.pack()

        self.timer_window = tk.Toplevel(master)
        self.timer_window.title("Таймер")
        self.timer_window.geometry("1024x768")
        self.timer_window['bg'] = 'black'
        self.timer_window.withdraw()

        self.timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 100), bg="black", fg="red")
        self.timer_label.pack(expand=True)
        self.timer_label.place(relx=0.5, rely=0.355, anchor="center")

        self.team1_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team1_label.place(relx=0.2, rely=0.1, anchor="center")
        self.team2_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team2_label.place(relx=0.8, rely=0.1, anchor="center")

        self.timer_running = False
        self.time_remaining = 20 * 60
        self.start_time = 0
        self.paused_time = 0

####################################

        self.penalty_timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label.pack(expand=True)
        self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")

        self.penalty_timer_running = False
        self.penalty_time_remaining = 20 * 60
        self.penalty_start_time = 0
        self.penalty_paused_time = 0



###################################


        ###############################################  ПЕРЕМЕННЫЕ  ###########################################
        self.goal_home_var = tk.IntVar(value=0)
        self.goal_home_label = tk.Label(self.timer_window, textvariable=self.goal_home_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_home_label.place(relx=0.2, rely=0.3, anchor="center")

        self.goal_away_var = tk.IntVar(value=0)
        self.goal_away_label = tk.Label(self.timer_window, textvariable=self.goal_away_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_away_label.place(relx=0.8, rely=0.3, anchor="center")

        self.period_var = tk.IntVar(value=1)
        self.period_var_label = tk.Label(self.timer_window, textvariable=self.period_var, font=("DS-Digital", 100), bg="black", fg="green")
        self.period_var_label.place(relx=0.5, rely=0.68, anchor="center")

        ##############################################   ТЕКСТЫ LABLES #######################################
            #Текст таймера таймаута team1
        self.timeout_team1_label = tk.Label(self.timer_window, text="", font=("DS-Digital", 30), bg="black", fg="yellow")
        self.timeout_team1_label.place(relx=0.2, rely=0.49, anchor="center")
        # self.timeout_team1_label.pack()

            #Текст таймера таймаута team2
        self.timeout_team2_label = tk.Label(self.timer_window, text="", font=("DS-Digital", 30), bg="black", fg="yellow")
        self.timeout_team2_label.place(relx=0.8, rely=0.49, anchor="center")
        # self.timeout_team1_label.pack()

            #Текст ВРЕМЯ по центру
        self.time_text_label = tk.Label(self.timer_window, text="ТАЙМЕР", font=("Helvetica", 30), bg="black", fg="white")
        self.time_text_label.place(relx=0.5, rely=0.25, anchor="center")

            # Текст ПЕРИОД по центру
        self.time_text_label = tk.Label(self.timer_window, text="ПЕРИОД", font=("Helvetica", 25), bg="black", fg="white")
        self.time_text_label.place(relx=0.5, rely=0.55, anchor="center")


        self.break_time = tk.Label(self.timer_window, text="", font=("DS-Digital", 45), bg="black", fg="white")
        self.break_time.place(relx=0.5, rely=0.87, anchor="center")
        # self.break_time.pack()

            # Текст УДАЛЕНИЯ по БОКАМ
        self.time_text_label = tk.Label(self.timer_window, text="УДАЛЕНИЯ", font=("Helvetica", 25), bg="black", fg="white")
        self.time_text_label.place(relx=0.2, rely=0.55, anchor="center")
        self.time_text_label2 = tk.Label(self.timer_window, text="УДАЛЕНИЯ", font=("Helvetica", 25), bg="black", fg="white")
        self.time_text_label2.place(relx=0.8, rely=0.55, anchor="center")

            #Текст ХОЗЯЕВА и ГОСТИ
        self.time_text_label = tk.Label(self.timer_window, text="ХОЗЯЕВА", font=("Helvetica", 15), bg="black", fg="white")
        self.time_text_label.place(relx=0.2, rely=0.03, anchor="center")
        self.time_text_label2 = tk.Label(self.timer_window, text="ГОСТИ", font=("Helvetica", 15), bg="black", fg="white")
        self.time_text_label2.place(relx=0.8, rely=0.03, anchor="center")


        #######################################   КНОПКИ в окне master   ##########################################
        self.save_teams_button = tk.Button(master, text="Записать команды", command=self.save_teams)
        self.save_teams_button.pack()

        self.button = tk.Button(master, text="Игра", command=self.toggle_timer)
        self.button.pack()

        self.reset_button = tk.Button(master, text="Начать сначала", command=self.reset_timer)
        self.reset_button.pack()

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

        self.fullscreen_button = tk.Button(master, text="Вывести на табло", command=self.fullscreen_timer)
        self.fullscreen_button.pack()

        #Кнопка перерыва между периодами
        self.button_break = tk.Button(self.master, text="Перерыв", command=self.start_break_timer)
        self.button_break.pack()

        self.break_label = None

        #Кнопка таймаут team1
        self.timeout_team1_button = tk.Button(self.master, text="Таймаут хозяева", command=self.start_timeout_team1)
        self.timeout_team1_button.pack()

        self.timeout_label_team1 = None

        #Кнопка таймаут team2
        self.timeout_team2_button = tk.Button(self.master, text="Таймаут гости", command=self.start_timeout_team2)
        self.timeout_team2_button.pack()

        self.timeout_label_team2 = None

        # Кнопка включения ТАБЛО
        self.on_tablo_button = tk.Button(self.master, text="ВКЛ. Табло", command=self.on_tablo)
        self.on_tablo_button.pack()

        # Кнопка выключения ТАБЛО
        self.off_tablo_button = tk.Button(self.master, text="ВЫКЛ. Табло", command=self.off_tablo)
        self.off_tablo_button.pack()
        self.off_tablo_button.config(state=tk.DISABLED)
        ####################

        self.fullscreen_state = False

        ###########################################Горячие КЛАВИШИ  #######################################
        self.master.bind("<space>", self.toggle_timer_space)
        self.master.bind("<Return>", self.toggle_timer_enter)

        self.update_timer()
        self.penalty_update_timer()


####################################### тест штрафных
        # Добавление полей ввода для номера игрока и штрафных минут
        self.player_number_entry = tk.Entry(master)
        self.player_number_entry.pack()

        self.penalty_minutes_entry = tk.Entry(master)
        self.penalty_minutes_entry.pack()

        # Кнопка "Штраф"
        self.penalty_button = tk.Button(master, text="Игра", command=self.penalty_toggle_timer)
        self.penalty_button.pack()

    def penalty_toggle_timer(self):
        if self.penalty_timer_running:
            self.penalty_timer_running = False
            self.penalty_button.config(text="Игра")
            self.penalty_paused_time = time.time() - self.penalty_start_time
        else:
            if self.penalty_time_remaining == 0:
                self.penalty_time_remaining = 20 * 60
            self.penalty_timer_running = True
            self.penalty_button.config(text="Пауза")
            self.penalty_start_time = time.time() - (20 * 60 - self.penalty_time_remaining)
            self.penalty_update_timer()

    def penalty_update_timer(self):
        if self.penalty_timer_running:
            elapsed_time = int(time.time() - self.penalty_start_time)
            self.penalty_time_remaining = max(0, 20 * 60 - elapsed_time)
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))
            if self.penalty_time_remaining > 0:
                self.timer_window.after(1000, self.penalty_update_timer)
            else:
                self.penalty_timer_running = False
                self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))

    def penalty_format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)

################################### КОНЕЦ тест штрафных

    ##########################################  ФУНКЦИИ ###################################################

    def on_tablo(self):
        self.timer_window.deiconify()
        self.off_tablo_button.config(state=tk.NORMAL)
        self.on_tablo_button.config(state=tk.DISABLED)

    def off_tablo(self):
        self.timer_window.withdraw()
        self.off_tablo_button.config(state=tk.DISABLED)
        self.on_tablo_button.config(state=tk.NORMAL)

    # Таймаут функция team1
    def start_timeout_team1(self):
        self.timeout_team1_label.config(text="00:00")
        self.timeout_team1_button.config(state=tk.DISABLED)

        self.timeout_label_team1 = tk.Label(self.timer_window, text="ТАЙМАУТ", font=("Helvetika", 16), bg="black", fg="white")
        self.timeout_label_team1.place(relx=0.2, rely=0.45, anchor="center")
        # self.timeout_label_team1.pack(pady=10)

        self.countdown_team1(1 * 30)

    def countdown_team1(self, remaining_time):
        if remaining_time <= 0:
            self.timeout_team1_label.config(text="")
            self.timeout_team1_button.config(state=tk.NORMAL)
            if self.timeout_label_team1:
                self.timeout_label_team1.place_forget()
                self.timeout_label_team1 = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.timeout_team1_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.master.after(1000, self.countdown_team1, remaining_time - 1)

    # Таймаут функция team2
    def start_timeout_team2(self):
        self.timeout_team2_label.config(text="00:00")
        self.timeout_team2_button.config(state=tk.DISABLED)

        self.timeout_label_team2 = tk.Label(self.timer_window, text="ТАЙМАУТ", font=("Helvetika", 16), bg="black", fg="white")
        self.timeout_label_team2.place(relx=0.8, rely=0.45, anchor="center")
        # self.timeout_label_team1.pack(pady=10)

        self.countdown_team2(1 * 30)

    def countdown_team2(self, remaining_time):
        if remaining_time <= 0:
            self.timeout_team2_label.config(text="")
            self.timeout_team2_button.config(state=tk.NORMAL)
            if self.timeout_label_team2:
                self.timeout_label_team2.place_forget()
                self.timeout_label_team2 = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.timeout_team2_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.master.after(1000, self.countdown_team2, remaining_time - 1)
    ############# КОНЕЦ функции таймаут

    #Таймер перерыва 17 минут
    def start_break_timer(self):
        self.break_time.config(text="00:00")
        self.button_break.config(state=tk.DISABLED)

        self.break_label = tk.Label(self.timer_window, text="ПЕРЕРЫВ", font=("Helvetica", 25), bg="black", fg="white")
        self.break_label.place(relx=0.5, rely=0.80, anchor="center")
        # self.break_label.pack(pady=20)


        self.countdown_break(1 * 6) # Установка времени перерыва, пример: 17 * 60 = 17 минут

    def countdown_break(self, remaining_time):
        if remaining_time <= 0:
            self.break_time.config(text="")
            self.button_break.config(state=tk.NORMAL)
            if self.break_label:
                self.break_label.place_forget()
                self.break_label = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.break_time.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.timer_window.after(1000, self.countdown_break, remaining_time - 1)
    ###############  КОНЕЦ Таймер перерыва 17 минут

    def toggle_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.button.config(text="Игра")
            self.paused_time = time.time() - self.start_time
        else:
            if self.time_remaining == 0:
                self.time_remaining = 20 * 60
            self.timer_running = True
            self.button.config(text="Пауза")
            self.start_time = time.time() - (20 * 60 - self.time_remaining)
            self.update_timer()


    def toggle_timer_space(self, event):
        self.toggle_timer()

    def toggle_timer_enter(self, event):
        self.save_teams()

    def reset_timer(self):
        self.timer_running = False
        self.button.config(text="Игра")
        self.time_remaining = 20 * 60
        self.timer_label.config(text=self.format_time(self.time_remaining))
        self.start_time = 0
        self.paused_time = 0

    def save_teams(self):
        if not self.timer_running:
            team1_name = self.team1_name_entry.get()
            team2_name = self.team2_name_entry.get()
            self.team1_label.config(text=team1_name.upper())
            self.team2_label.config(text=team2_name.upper())

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
            self.fullscreen_button.config(text="Не выводить на табло")
        else:
            self.timer_window.attributes("-fullscreen", False)
            self.fullscreen_state = False
            self.timer_window.withdraw()
            self.fullscreen_button.config(text="Вывести на табло")

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
