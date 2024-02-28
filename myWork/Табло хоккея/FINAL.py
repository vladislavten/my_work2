import tkinter as tk
from tkinter import messagebox
import time
from screeninfo import get_monitors


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Управление Таймером")
        self.master.geometry("600x800")

        # self.new_window = tk.Toplevel(master)
        # self.new_window.title("Управление Таймером")
        # self.new_window.geometry('600x600')



        # Добавляем поля ввода для имен команд и кнопку "Сохранить команды"
        self.team1_name_entry = tk.Entry(master)
        self.team1_name_entry.pack()
        self.team2_name_entry = tk.Entry(master)
        self.team2_name_entry.pack()

        self.monitors = get_monitors()
        # Выбираем второй монитор (индекс 1)
        if len(self.monitors) < 2:
            messagebox.showinfo('INFO', 'Табло не обнаружено')
            self.secondary_monitor = self.monitors[0]
        else:
            self.secondary_monitor = self.monitors[1]

        self.timer_window = tk.Toplevel(master)
        self.timer_window.title("Таймер")
        self.timer_window.geometry(
            f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
        self.timer_window['bg'] = 'black'
        self.timer_window.overrideredirect(True)
        self.timer_window.withdraw()

        self.timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 100), bg="black", fg="red")
        self.timer_label.pack(expand=True)
        self.timer_label.place(relx=0.5, rely=0.355, anchor="center")

        self.timer_running = False
        self.time_remaining = 1 * 10
        self.start_time = 0
        self.paused_time = 0

##############################################
        ### ШТРАФНОЙ
        self.penalty_timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
        self.penalty_timer_label.place_forget()

        self.penalty_timer_running = False
        self.penalty_time_remaining = 0 # БЫЛО 20 * 60
        self.penalty_start_time = 0
        self.penalty_paused_time = 0

        self.penalty_number_label = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label.place(relx=0.7, rely=0.8, anchor="center")
        self.penalty_timer_label.place_forget()

        ### ШТРАФНОЙ 2
        self.penalty_timer_label2 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label2.place(relx=0.9, rely=0.8, anchor="center")
        self.penalty_timer_label2.place_forget()

        self.penalty_timer_running2 = False
        self.penalty_time_remaining2 = 0 # БЫЛО 20 * 60
        self.penalty_start_time2 = 0
        self.penalty_paused_time2 = 0

        self.penalty_number_label2 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label2.place(relx=0.5, rely=0.8, anchor="center")
        self.penalty_timer_label2.place_forget()


        ### ШТРАФНОЙ 3
        self.penalty_timer_label3 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label3.place(relx=0.9, rely=0.8, anchor="center")
        self.penalty_timer_label3.place_forget()

        self.penalty_timer_running3 = False
        self.penalty_time_remaining3 = 0 # БЫЛО 20 * 60
        self.penalty_start_time3 = 0
        self.penalty_paused_time3 = 0

        self.penalty_number_label3 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label3.place(relx=0.5, rely=0.8, anchor="center")
        self.penalty_timer_label3.place_forget()

        ### ШТРАФНОЙ 4
        self.penalty_timer_label4 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label4.place(relx=0.9, rely=0.8, anchor="center")
        self.penalty_timer_label4.place_forget()

        self.penalty_timer_running4 = False
        self.penalty_time_remaining4 = 0  # БЫЛО 20 * 60
        self.penalty_start_time4 = 0
        self.penalty_paused_time4 = 0

        self.penalty_number_label4 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label4.place(relx=0.7, rely=0.8, anchor="center")
        self.penalty_timer_label4.place_forget()

        ############################


        ###############################################  ПЕРЕМЕННЫЕ  ###########################################

#######################################
        self.penalty_minutes = '0'
        self.penalty_minutes2 = '0'
        self.penalty_minutes3 = '0'
        self.penalty_minutes4 = '0'

#######################################

        self.goal_home_var = tk.IntVar(value=0)
        self.goal_home_label = tk.Label(self.timer_window, textvariable=self.goal_home_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_home_label.place(relx=0.2, rely=0.3, anchor="center")

        self.goal_away_var = tk.IntVar(value=0)
        self.goal_away_label = tk.Label(self.timer_window, textvariable=self.goal_away_var, font=("DS-Digital", 200), bg="black", fg="red")
        self.goal_away_label.place(relx=0.8, rely=0.3, anchor="center")

        self.team1_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team1_label.place(relx=0.2, rely=0.1, anchor="center")
        self.team2_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team2_label.place(relx=0.8, rely=0.1, anchor="center")

        self.period_var = tk.IntVar(value=1)
        self.period_var_label = tk.Label(self.timer_window, textvariable=self.period_var, font=("DS-Digital", 100), bg="black", fg="green")
        self.period_var_label.place(relx=0.5, rely=0.68, anchor="center")

        ##############################################   ТЕКСТЫ LABLES #######################################
        self.name_team1_label = tk.Label(self.master, text= 'НАСТРОЙКА КОМАНД', font=("tahoma", 10))
        self.name_team1_label.place(x=20, y=10)

            #Текст таймера таймаута team1
        self.timeout_team1_label = tk.Label(self.timer_window, text="", font=("DS-Digital", 30), bg="black", fg="yellow")
        self.timeout_team1_label.place(relx=0.2, rely=0.49, anchor="center")
        # self.timeout_team1_label.pack()
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

        self.button = tk.Button(master, text="Игра", command=self.general_start)
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

######################################################
        self.penalty_button = tk.Button(master, text="Записать штраф 1", command=self.penalty_apply)
        self.penalty_button.pack()

        self.penalty_button2 = tk.Button(master, text="Записать штраф 2", command=self.penalty_apply2)
        self.penalty_button2.pack()

        self.penalty_button3 = tk.Button(master, text="Записать штраф 3", command=self.penalty_apply3)
        self.penalty_button3.pack()

        self.penalty_button4 = tk.Button(master, text="Записать штраф 4", command=self.penalty_apply4)
        self.penalty_button4.pack()


######################################################

#######################################  ВВОД ДАННЫХ В ОКНЕ MASTER #####################################

        self.penalty_minutes_entry = tk.Entry(master)
        self.penalty_minutes_entry.pack()

        self.penalty_number_entry = tk.Entry(master)
        self.penalty_number_entry.pack()

        self.penalty_update_timer()

        self.penalty_minutes_entry2 = tk.Entry(master)
        self.penalty_minutes_entry2.pack()

        self.penalty_number_entry2 = tk.Entry(master)
        self.penalty_number_entry2.pack()

        self.penalty_update_timer2()

        self.penalty_minutes_entry3 = tk.Entry(master)
        self.penalty_minutes_entry3.pack()

        self.penalty_number_entry3 = tk.Entry(master)
        self.penalty_number_entry3.pack()

        self.penalty_update_timer3()

        self.penalty_minutes_entry4 = tk.Entry(master)
        self.penalty_minutes_entry4.pack()

        self.penalty_number_entry4 = tk.Entry(master)
        self.penalty_number_entry4.pack()

        self.penalty_update_timer4()

        self.update_timer()

        ################################################################

        ###########################################Горячие КЛАВИШИ  #######################################
        self.master.bind("<space>", self.toggle_timer_space)
        self.master.bind("<Return>", self.toggle_timer_enter)

        self.update_timer()
        self.penalty_update_timer()

    ##########################################  ФУНКЦИИ ###################################################

####################################### тест штрафных
    def general_start(self):
        self.penalty_toggle_timer()
        self.penalty_toggle_timer2()
        self.penalty_toggle_timer3()
        self.penalty_toggle_timer4()

        self.toggle_timer()

    def penalty_apply(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry.get() == '2'
                    or self.penalty_minutes_entry.get() == '4'
                    or self.penalty_minutes_entry.get() == '5'):
                if not self.penalty_number_entry.get() == '':
                    # self.penalty_minutes = 0
                    self.penalty_timer_label.place_forget()
                    self.penalty_number_label.place_forget()
                    self.time_zero()  # сброс тайминга штрафа
                    self.penalty_minutes = self.penalty_minutes_entry.get()
                    self.penalty_timer_label = tk.Label(self.timer_window, text=f"0{self.penalty_minutes}:00",
                                                        font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
                    self.penalty_number = self.penalty_number_entry.get()
                    self.penalty_number_label = tk.Label(self.timer_window, text=self.penalty_number,
                                                         font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_number_label.place(relx=0.7, rely=0.8, anchor="center")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply2(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry2.get() == '2'
                    or self.penalty_minutes_entry2.get() == '4'
                    or self.penalty_minutes_entry2.get() == '5'):
                if not self.penalty_number_entry2.get() == '':
                    # self.penalty_minutes = 0
                    self.penalty_timer_label2.place_forget()
                    self.penalty_number_label2.place_forget()
                    self.time_zero2()  # сброс тайминга штрафа
                    self.penalty_minutes2 = self.penalty_minutes_entry2.get()
                    self.penalty_timer_label2 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes2}:00",
                                                         font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label2.place(relx=0.9, rely=0.7, anchor="center")
                    self.penalty_number2 = self.penalty_number_entry2.get()
                    self.penalty_number_label2 = tk.Label(self.timer_window, text=self.penalty_number2,
                                                          font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_number_label2.place(relx=0.7, rely=0.7, anchor="center")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply3(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry3.get() == '2'
                    or self.penalty_minutes_entry3.get() == '4'
                    or self.penalty_minutes_entry3.get() == '5'):
                if not self.penalty_number_entry3.get() == '':
                    # self.penalty_minutes = 0
                    self.penalty_timer_label3.place_forget()
                    self.penalty_number_label3.place_forget()
                    self.time_zero3()  # сброс тайминга штрафа
                    self.penalty_minutes3 = self.penalty_minutes_entry3.get()
                    self.penalty_timer_label3 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes3}:00",
                                                         font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label3.place(relx=0.9, rely=0.6, anchor="center")
                    self.penalty_number3 = self.penalty_number_entry3.get()
                    self.penalty_number_label3 = tk.Label(self.timer_window, text=self.penalty_number3,
                                                          font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_number_label3.place(relx=0.7, rely=0.6, anchor="center")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply4(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry4.get() == '2'
                    or self.penalty_minutes_entry4.get() == '4'
                    or self.penalty_minutes_entry4.get() == '5'):
                if not self.penalty_number_entry4.get() == '':
                    # self.penalty_minutes = 0
                    self.penalty_timer_label4.place_forget()
                    self.penalty_number_label4.place_forget()
                    self.time_zero4()  # сброс тайминга штрафа
                    self.penalty_minutes4 = self.penalty_minutes_entry4.get()
                    self.penalty_timer_label4 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes4}:00",
                                                         font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label4.place(relx=0.9, rely=0.5, anchor="center")
                    self.penalty_number4 = self.penalty_number_entry4.get()
                    self.penalty_number_label4 = tk.Label(self.timer_window, text=self.penalty_number4,
                                                          font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_number_label4.place(relx=0.7, rely=0.5, anchor="center")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def time_zero(self):
        self.penalty_time_remaining = 0  # БЫЛО 20 * 60
        self.penalty_start_time = 0
        self.penalty_paused_time = 0

    def time_zero2(self):
        self.penalty_time_remaining2 = 0  # БЫЛО 20 * 60
        self.penalty_start_time2 = 0
        self.penalty_paused_time2 = 0

    def time_zero3(self):
        self.penalty_time_remaining3 = 0  # БЫЛО 20 * 60
        self.penalty_start_time3 = 0
        self.penalty_paused_time3 = 0

    def time_zero4(self):
        self.penalty_time_remaining4 = 0  # БЫЛО 20 * 60
        self.penalty_start_time4 = 0
        self.penalty_paused_time4 = 0

    def penalty_toggle_timer(self):
        if self.penalty_timer_running:
            self.penalty_timer_running = False
            # self.penalty_button.config(text="Игра")
            self.penalty_paused_time = time.time() - self.penalty_start_time
        else:
            if self.penalty_time_remaining == 0:
                self.penalty_time_remaining = int(self.penalty_minutes) * 6
            self.penalty_timer_running = True
            # self.penalty_button.config(text="Пауза")
            self.penalty_start_time = time.time() - (int(self.penalty_minutes) * 6 - self.penalty_time_remaining)
            self.penalty_update_timer()

    def penalty_toggle_timer2(self):
        if self.penalty_timer_running2:
            self.penalty_timer_running2 = False
            # self.penalty_button.config(text="Игра")
            self.penalty_paused_time2 = time.time() - self.penalty_start_time2
        else:
            if self.penalty_time_remaining2 == 0:
                self.penalty_time_remaining2 = int(self.penalty_minutes2) * 6
            self.penalty_timer_running2 = True
            # self.penalty_button.config(text="Пауза")
            self.penalty_start_time2 = time.time() - (int(self.penalty_minutes2) * 6 - self.penalty_time_remaining2)
            self.penalty_update_timer2()

    def penalty_toggle_timer3(self):
        if self.penalty_timer_running3:
            self.penalty_timer_running3 = False
            # self.penalty_button.config(text="Игра")
            self.penalty_paused_time3 = time.time() - self.penalty_start_time3
        else:
            if self.penalty_time_remaining3 == 0:
                self.penalty_time_remaining3 = int(self.penalty_minutes3) * 6
            self.penalty_timer_running3 = True
            # self.penalty_button.config(text="Пауза")
            self.penalty_start_time3 = time.time() - (int(self.penalty_minutes3) * 6 - self.penalty_time_remaining3)
            self.penalty_update_timer3()

    def penalty_toggle_timer4(self):
        if self.penalty_timer_running4:
            self.penalty_timer_running4 = False
            # self.penalty_button.config(text="Игра")
            self.penalty_paused_time4 = time.time() - self.penalty_start_time4
        else:
            if self.penalty_time_remaining4 == 0:
                self.penalty_time_remaining4 = int(self.penalty_minutes4) * 6
            self.penalty_timer_running4 = True
            # self.penalty_button.config(text="Пауза")
            self.penalty_start_time4 = time.time() - (int(self.penalty_minutes4) * 6 - self.penalty_time_remaining4)
            self.penalty_update_timer4()

    def penalty_update_timer(self):
        if self.penalty_timer_running:
            elapsed_time = int(time.time() - self.penalty_start_time)
            self.penalty_time_remaining = max(0, int(self.penalty_minutes) * 6 - elapsed_time)
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))
            if self.penalty_time_remaining > 0:
                self.timer_window.after(1000, self.penalty_update_timer)
            else:
                self.penalty_timer_running = False
                self.penalty_timer_label.place_forget()
                self.penalty_minutes = '0'  # Обязательно возращать 0 во все переменные штрафа
                self.penalty_number_label.place_forget()

                # self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))

    def penalty_update_timer2(self):
        if self.penalty_timer_running2:
            elapsed_time2 = int(time.time() - self.penalty_start_time2)
            self.penalty_time_remaining2 = max(0, int(self.penalty_minutes2) * 6 - elapsed_time2)
            self.penalty_timer_label2.config(text=self.penalty_format_time2(self.penalty_time_remaining2))
            if self.penalty_time_remaining2 > 0:
                self.timer_window.after(1000, self.penalty_update_timer2)
            else:
                self.penalty_timer_running2 = False
                self.penalty_timer_label2.place_forget()
                self.penalty_minutes2 = '0'  # Обязательно возращать 0 во все переменные штрафа
                self.penalty_number_label2.place_forget()

                # self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label2.config(text=self.penalty_format_time2(self.penalty_time_remaining2))

    def penalty_update_timer3(self):
        if self.penalty_timer_running3:
            elapsed_time3 = int(time.time() - self.penalty_start_time3)
            self.penalty_time_remaining3 = max(0, int(self.penalty_minutes3) * 6 - elapsed_time3)
            self.penalty_timer_label3.config(text=self.penalty_format_time3(self.penalty_time_remaining3))
            if self.penalty_time_remaining3 > 0:
                self.timer_window.after(1000, self.penalty_update_timer3)
            else:
                self.penalty_timer_running3 = False
                self.penalty_timer_label3.place_forget()
                self.penalty_minutes3 = '0'  # Обязательно возращать 0 во все переменные штрафа
                self.penalty_number_label3.place_forget()

                # self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label3.config(text=self.penalty_format_time3(self.penalty_time_remaining3))

    def penalty_update_timer4(self):
        if self.penalty_timer_running4:
            elapsed_time4 = int(time.time() - self.penalty_start_time4)
            self.penalty_time_remaining4 = max(0, int(self.penalty_minutes4) * 6 - elapsed_time4)
            self.penalty_timer_label4.config(text=self.penalty_format_time4(self.penalty_time_remaining4))
            if self.penalty_time_remaining4 > 0:
                self.timer_window.after(1000, self.penalty_update_timer4)
            else:
                self.penalty_timer_running4 = False
                self.penalty_timer_label4.place_forget()
                self.penalty_minutes4 = '0'  # Обязательно возращать 0 во все переменные штрафа
                self.penalty_number_label4.place_forget()

                # self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))

    def penalty_format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)

    def penalty_format_time2(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)

    def penalty_format_time3(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)

    def penalty_format_time4(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)

################################### КОНЕЦ тест штрафных


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

    def toggle_timer_space(self, event):
        self.general_start()

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

    def toggle_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.button.config(text="Игра")
            self.paused_time = time.time() - self.start_time
        else:
            if self.time_remaining <= 0:
                self.time_remaining = 20 * 60
            self.timer_running = True
            self.button.config(text="Пауза")
            self.start_time = time.time() - (20 * 60 - self.time_remaining)
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            # print(self.time_remaining)
            elapsed_time = int(time.time() - self.start_time)
            self.time_remaining = max(0, 20 * 60 - elapsed_time)
            self.timer_label.config(text=self.format_time(self.time_remaining))
            if self.time_remaining > 0:
                self.timer_window.after(1000, self.update_timer)
            else:
                print('Меньше нуля')
                self.general_start()
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
