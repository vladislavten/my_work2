import time
import tkinter as tk
from tkinter import messagebox
from screeninfo import get_monitors
from PIL import Image, ImageTk
import os.path
from tkinter import ttk
import pickle
from stopwatch import Stopwatch
import pygame



def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите завершить работу программы: Управление таймером?"):
        root.destroy()


class TimerApp:
    def __init__(self, master):
        self.monitors = get_monitors()
        # Выбираем второй монитор (индекс 1)pip install pillow
        if len(self.monitors) < 2:
            messagebox.showinfo('INFO', 'Табло не обнаружено')
            self.secondary_monitor = self.monitors[0]
        else:
            print(len(self.monitors))
            self.secondary_monitor = self.monitors[1]  # 1 это второй монитор, 0 это первый

        self.master = master
        self.master.title("Управление Таймером")
        self.master.geometry('900x757')
        self.master.resizable(False, False)
        self.master['bg'] = 'lightblue'

        if os.path.exists('icon.ico'):
            root.iconbitmap("icon.ico")



        ################################ ДЕКОРАЦИИ ##################################################
        black_strip = tk.Frame(self.master, bg="black", width=900, height=260)
        black_strip.pack(side="top")

        green_strip = tk.Frame(self.master, bg="green", width=900, height=58)
        green_strip.pack(side="bottom")

        white_strip = tk.Frame(self.master, bg="white", width=900, height=1)
        white_strip.place(x=0, y=328)
        white_strip = tk.Frame(self.master, bg="white", width=1, height=250)
        white_strip.place(x=449, y=329)
        white_strip = tk.Frame(self.master, bg="white", width=900, height=1)
        white_strip.place(x=0, y=407)
        white_strip = tk.Frame(self.master, bg="white", width=900, height=1)
        white_strip.place(x=0, y=578)
        white_strip = tk.Frame(self.master, bg="white", width=1, height=120)
        white_strip.place(x=673, y=579)
        white_strip = tk.Frame(self.master, bg="white", width=1, height=120)
        white_strip.place(x=223, y=579)
        ##############################################################################################

        # Добавляем поля ввода для имен команд и кнопку "Сохранить команды"
        self.team1_name_entry = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.team1_name_entry.place(x=215, y=302, anchor='center', width=180, height=25)
        self.team2_name_entry = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.team2_name_entry.place(x=675, y=302, anchor='center', width=180, height=25)

        self.timer_window = tk.Toplevel(master)
        self.timer_window.title("Таймер")
        self.timer_window.geometry(
            f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
        # self.timer_window.geometry('1024x768')
        # self.timer_window.geometry('1280x1024')
        self.timer_window['bg'] = 'black'
        self.timer_window.overrideredirect(True)
        # self.timer_window.attributes('-topmost', True)
        self.timer_window.withdraw()

        self.timer_label = tk.Label(self.timer_window, text="20:00", font=("DS-Digital", 100), bg="black", fg="red")
        self.timer_label.place(relx=0.5, rely=0.295, anchor="center")

        self.timer_label_control = tk.Label(self.master, text="20:00", font=("DS-Digital", 30), bg="black", fg="red")
        self.timer_label_control.place(x=450, y=105, anchor="center")

        self.timer_running = False

        ##############################################
        ### ШТРАФНОЙ
        self.penalty_timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                            fg="red")
        self.penalty_timer_label_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                    fg="red")

        self.penalty_number_label = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_number_label_control = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_timer = Stopwatch()

        ### ШТРАФНОЙ 2
        self.penalty_timer_label2 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_timer_label2_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_number_label2 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                              fg="red")
        self.penalty_number_label2_control = tk.Label(self.master, text=False, font=("DS-Digital", 40), bg="black",
                                                      fg="red")

        self.penalty_timer2 = Stopwatch()

        ### ШТРАФНОЙ 3
        self.penalty_timer_label3 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_timer_label3_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_number_label3 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                              fg="red")
        self.penalty_number_label3_control = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40),
                                                      bg="black", fg="red")

        self.penalty_timer3 = Stopwatch()

        ### ШТРАФНОЙ 4
        self.penalty_timer_label4 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_timer_label4_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_number_label4 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                              fg="red")
        self.penalty_number_label4_control = tk.Label(self.master, text=False, font=("DS-Digital", 40), bg="black",
                                                      fg="red")

        self.penalty_timer4 = Stopwatch()

        ### ШТРАФНОЙ 5
        self.penalty_timer_label5 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_timer_label5_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_number_label5 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                              fg="red")
        self.penalty_number_label5_control = tk.Label(self.master, text=False, font=("DS-Digital", 40), bg="black",
                                                      fg="red")

        self.penalty_timer5 = Stopwatch()

        ### ШТРАФНОЙ 6
        self.penalty_timer_label6 = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black",
                                             fg="red")
        self.penalty_timer_label6_control = tk.Label(self.master, text="00:00", font=("DS-Digital", 40), bg="black",
                                                     fg="red")

        self.penalty_number_label6 = tk.Label(self.timer_window, text=False, font=("DS-Digital", 40), bg="black",
                                              fg="red")
        self.penalty_number_label6_control = tk.Label(self.master, text=False, font=("DS-Digital", 40), bg="black",
                                                      fg="red")

        self.penalty_timer6 = Stopwatch()

        ############################

        ###############################################  ПЕРЕМЕННЫЕ  ###########################################

        #######################################

        self.data_team = {}
        self.data_team2 = {}
        try:
            with open("data_team_home.pkl", "rb") as f:
                self.data_team = pickle.load(f)
            with open("data_team_guest.pkl", "rb") as f:
                self.data_team2 = pickle.load(f)
        except:
            pass

        #######################################

        self.goal_home_var = tk.IntVar(value=0)
        self.goal_home_label = tk.Label(self.timer_window, textvariable=self.goal_home_var, font=("DS-Digital", 200),
                                        bg="black", fg="red")
        self.goal_home_label.place(relx=0.2, rely=0.25, anchor="center")

        self.goal_home_label = tk.Label(self.master, textvariable=self.goal_home_var, font=("DS-Digital", 58),
                                        bg="black", fg="red")
        self.goal_home_label.place(x=215, y=88, anchor="center")

        self.goal_away_var = tk.IntVar(value=0)
        self.goal_away_label = tk.Label(self.timer_window, textvariable=self.goal_away_var, font=("DS-Digital", 200),
                                        bg="black", fg="red")
        self.goal_away_label.place(relx=0.8, rely=0.25, anchor="center")

        self.goal_away_label = tk.Label(self.master, textvariable=self.goal_away_var, font=("DS-Digital", 58),
                                        bg="black", fg="red")
        self.goal_away_label.place(x=673, y=88, anchor="center")

        self.team1_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team1_label.place(relx=0.2, rely=0.1, anchor="center")
        self.team1_label_control = tk.Label(self.master, text="", font=("Helvetica", 18), bg="black", fg="white")
        self.team1_label_control.place(x=215, y=40, anchor="center")
        self.team2_label = tk.Label(self.timer_window, text="", font=("Helvetica", 40, "bold"), bg="black", fg="white")
        self.team2_label.place(relx=0.8, rely=0.1, anchor="center")
        self.team2_label_control = tk.Label(self.master, text="", font=("Helvetica", 18), bg="black", fg="white")
        self.team2_label_control.place(x=674, y=40, anchor="center")

        self.period_var = tk.IntVar(value=1)
        self.period_var_label = tk.Label(self.timer_window, textvariable=self.period_var, font=("DS-Digital", 120),
                                         bg="black", fg="#12e802")
        self.period_var_label.place(relx=0.5, rely=0.68, anchor="center")
        self.period_var_label = tk.Label(self.master, textvariable=self.period_var, font=("DS-Digital", 30), bg="black",
                                         fg="#12e802")
        self.period_var_label.place(x=450, y=185, anchor="center")

        ##############################################   ТЕКСТЫ LABLES #######################################
        self.name_team2_label = tk.Label(self.master, text='НАЗВАНИЕ КОМАНДЫ ХОЗЯЕВ', font=("Helvetica", 8), fg='black',
                                         bg='lightblue')
        self.name_team2_label.place(x=215, y=274, anchor='center')

        self.name_team1_label = tk.Label(self.master, text='НАЗВАНИЕ КОМАНДЫ ГОСТЕЙ', font=("Helvetica", 8), fg='black',
                                         bg='lightblue')
        self.name_team1_label.place(x=675, y=274, anchor='center')

        self.control_team1_label = tk.Label(self.master, text='УПРАВЛЕНИЕ КОМАНДОЙ ХОЗЯЕВ', font=("Helvetica", 8),
                                            fg='black', bg='lightblue')
        self.control_team1_label.place(x=215, y=345, anchor='center')
        self.control_team1_label.place(x=215, y=345, anchor='center')

        self.control_team1_label = tk.Label(self.master, text='УПРАВЛЕНИЕ КОМАНДОЙ ГОСТЕЙ', font=("Helvetica", 8),
                                            fg='black', bg='lightblue')
        self.control_team1_label.place(x=674, y=345, anchor='center')

        self.penalty_team1_label = tk.Label(self.master, text='ШТРАФЫ', font=("Helvetica", 8), fg='black',
                                            bg='lightblue')
        self.penalty_team1_label.place(x=215, y=425, anchor='center')

        self.penalty_team1_label = tk.Label(self.master, text='ШТРАФЫ', font=("Helvetica", 8), fg='black',
                                            bg='lightblue')
        self.penalty_team1_label.place(x=665, y=425, anchor='center')

        self.number1 = tk.Label(self.master, text='1.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number1.place(x=49, y=461, anchor='center')
        self.number1 = tk.Label(self.master, text='2.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number1.place(x=49, y=505, anchor='center')
        self.number1 = tk.Label(self.master, text='3.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number1.place(x=49, y=548, anchor='center')

        self.number2 = tk.Label(self.master, text='1.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number2.place(x=496, y=461, anchor='center')
        self.number2 = tk.Label(self.master, text='2.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number2.place(x=496, y=505, anchor='center')
        self.number2 = tk.Label(self.master, text='3.  НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number2.place(x=496, y=548, anchor='center')

        self.minutes1 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes1.place(x=154, y=461, anchor='center')
        self.minutes1 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes1.place(x=154, y=505, anchor='center')
        self.minutes1 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes1.place(x=154, y=548, anchor='center')

        self.minutes2 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes2.place(x=604, y=461, anchor='center')
        self.minutes2 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes2.place(x=604, y=505, anchor='center')
        self.minutes2 = tk.Label(self.master, text='МИНУТЫ', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.minutes2.place(x=604, y=548, anchor='center')

        self.control_penalty_label = tk.Label(self.master, text='УПРАВЛЕНИЕ ТАЙМЕРОМ', font=("Helvetica", 8),
                                              fg='black', bg='lightblue')
        self.control_penalty_label.place(x=450, y=595, anchor='center')

        self.control_goal_label = tk.Label(self.master, text='ГОЛ ЗАБИЛ', font=("Helvetica", 8), fg='black',
                                           bg='lightblue')
        self.control_goal_label.place(x=114, y=595, anchor='center')

        self.control_goal_label2 = tk.Label(self.master, text='ГОЛ ЗАБИЛ', font=("Helvetica", 8), fg='black',
                                            bg='lightblue')
        self.control_goal_label2.place(x=785, y=595, anchor='center')

        # Текст таймера таймаута team1
        self.timeout_team1_label = tk.Label(self.timer_window, text="", font=("DS-Digital", 40), bg="black",
                                            fg="yellow")
        self.timeout_team1_label.place(relx=0.2, rely=0.49, anchor="center")
        self.timeout_team1_label_control = tk.Label(self.master, text="", font=("DS-Digital", 19), bg="black",
                                                    fg="yellow")
        self.timeout_team1_label_control.place(x=215, y=141, anchor="center")

        # Текст таймера таймаута team2
        self.timeout_team2_label = tk.Label(self.timer_window, text="", font=("DS-Digital", 40), bg="black",
                                            fg="yellow")
        self.timeout_team2_label.place(relx=0.8, rely=0.49, anchor="center")
        self.timeout_team2_label_control = tk.Label(self.master, text="", font=("DS-Digital", 19), bg="black",
                                                    fg="yellow")
        self.timeout_team2_label_control.place(x=674, y=141, anchor="center")

        # Текст ВРЕМЯ по центру
        self.time_text_label = tk.Label(self.timer_window, text="ТАЙМЕР", font=("Helvetica", 30), bg="black",
                                        fg="white")
        self.time_text_label.place(relx=0.5, rely=0.22, anchor="center")
        # self.time_text_label.place(relx=0.5, rely=0.25, anchor="center") #Так было
        self.time_text_label = tk.Label(self.master, text="ТАЙМЕР", font=("Helvetica", 10), bg="black", fg="white")
        self.time_text_label.place(x=450, y=78, anchor="center")

        # Текст ПЕРИОД по центру
        self.time_text_label = tk.Label(self.timer_window, text="ПЕРИОД", font=("Helvetica", 25), bg="black",
                                        fg="white")
        self.time_text_label.place(relx=0.5, rely=0.55, anchor="center")
        self.time_text_label = tk.Label(self.master, text="ПЕРИОД", font=("Helvetica", 10), bg="black", fg="white")
        self.time_text_label.place(x=450, y=154, anchor="center")

        self.break_time = tk.Label(self.timer_window, text="", font=("DS-Digital", 65), bg="black", fg="yellow")
        self.break_time.place(relx=0.5, rely=0.87, anchor="center")
        self.break_time_control = tk.Label(self.master, text="", font=("DS-Digital", 18), bg="black", fg="yellow")
        self.break_time_control.place(x=450, y=244, anchor="center")

        # Текст УДАЛЕНИЯ по БОКАМ
        self.time_text_label = tk.Label(self.timer_window, text="УДАЛЕНИЯ", font=("Helvetica", 25), bg="black",
                                        fg="white")
        self.time_text_label.place(relx=0.2, rely=0.55, anchor="center")
        self.time_text_label2 = tk.Label(self.timer_window, text="УДАЛЕНИЯ", font=("Helvetica", 25), bg="black",
                                         fg="white")
        self.time_text_label2.place(relx=0.8, rely=0.55, anchor="center")

        self.time_text_label_control = tk.Label(self.master, text="УДАЛЕНИЯ", font=("Helvetica", 12), bg="black",
                                                fg="white")
        self.time_text_label_control.place(x=216, y=164, anchor="center")
        self.time_text_label2_control = tk.Label(self.master, text="УДАЛЕНИЯ", font=("Helvetica", 12), bg="black",
                                                 fg="white")
        self.time_text_label2_control.place(x=673, y=164, anchor="center")

        # Текст ХОЗЯЕВА и ГОСТИ
        self.time_text_label = tk.Label(self.timer_window, text="ХОЗЯЕВА", font=("Helvetica", 15), bg="black",
                                        fg="white")
        self.time_text_label.place(relx=0.2, rely=0.03, anchor="center")

        self.time_text_label = tk.Label(self.master, text="ХОЗЯЕВА", font=("Helvetica", 9), bg="black", fg="white")
        self.time_text_label.place(x=189, y=5, anchor="nw")

        self.time_text_label2 = tk.Label(self.timer_window, text="ГОСТИ", font=("Helvetica", 15), bg="black",
                                         fg="white")
        self.time_text_label2.place(relx=0.8, rely=0.03, anchor="center")

        self.time_text_label2 = tk.Label(self.master, text="ГОСТИ", font=("Helvetica", 9), bg="black", fg="white")
        self.time_text_label2.place(x=652, y=5, anchor="nw")

        #######################################   КНОПКИ в окне master   ##########################################
        self.save_teams_button = tk.Button(self.master, text="ЗАПИСАТЬ КОМАНДЫ", width=20, command=self.save_teams)
        self.save_teams_button.place(x=450, y=302, anchor='center')

        self.button = tk.Button(self.master, text="ИГРА", width=12, command=self.general_start, bg='lightgreen', fg='black')
        self.button.place(x=65, y=729, anchor='center')

        self.reset_button = tk.Button(self.master, text="НАЧАТЬ СНАЧАЛА", width=15, command=self.reset_timer)
        self.reset_button.place(x=193, y=728, anchor='center')

        self.goal_home_increase_button = tk.Button(self.master, text="ГОЛ", width=16, command=self.goal_home_increase)
        self.goal_home_increase_button.place(x=82, y=375, anchor='center')

        self.goal_home_decrease_button = tk.Button(self.master, text="ГОЛ (-1)", width=16,
                                                   command=self.goal_home_decrease)
        self.goal_home_decrease_button.place(x=224, y=375, anchor='center')

        self.goal_away_increase_button = tk.Button(self.master, text="ГОЛ", width=16, command=self.goal_away_increase)
        self.goal_away_increase_button.place(x=532, y=375, anchor='center')

        self.goal_away_decrease_button = tk.Button(self.master, text="ГОЛ (-1)", width=16,
                                                   command=self.goal_away_decrease)
        self.goal_away_decrease_button.place(x=674, y=375, anchor='center')

        self.add_minute_button = tk.Button(self.master, text="+1 МИНУТА", width=12, command=self.add_minute)
        self.add_minute_button.place(x=290, y=626, anchor='center')

        self.subtract_minute_button = tk.Button(self.master, text="-1 МИНУТА", width=12, command=self.subtract_minute)
        self.subtract_minute_button.place(x=397, y=626, anchor='center')

        self.add_second_button = tk.Button(self.master, text="+1 СЕКУНДА", width=12, command=self.add_second)
        self.add_second_button.place(x=504, y=626, anchor='center')

        self.subtract_second_button = tk.Button(self.master, text="-1 СЕКУНДА", width=12, command=self.subtract_second)
        self.subtract_second_button.place(x=611, y=626, anchor='center')

        self.period_increase_button = tk.Button(self.master, text="+1 ПЕРИОД", width=12, command=self.period_increase)
        self.period_increase_button.place(x=290, y=668, anchor='center')

        self.goal_home_decrease_button = tk.Button(self.master, text="-1 ПЕРИОД", width=12,
                                                   command=self.period_decrease)
        self.goal_home_decrease_button.place(x=397, y=668, anchor='center')

        # Кнопка перерыва между периодами
        self.button_break = tk.Button(self.master, text="ПЕРЕРЫВ", width=12, command=self.start_break_timer,
                                      bg='yellow')
        self.button_break.place(x=504, y=668, anchor='center')

        self.button_cancel_break = tk.Button(self.master, text="ОТМЕНА", width=12, command=self.cancel_break_timer,
                                             bg='red', fg='white')
        self.button_cancel_break.place(x=611, y=668, anchor='center')

        self.break_label = None

        # Кнопка таймаут team1
        self.timeout_team1_button = tk.Button(self.master, text="ТАЙМАУТ", width=16, bg='yellow',
                                              command=self.start_timeout_team1)
        self.timeout_team1_button.place(x=366, y=375, anchor='center')

        self.timeout_label_team1 = None

        # Кнопка таймаут team2
        self.timeout_team2_button = tk.Button(self.master, text="ТАЙМАУТ", width=16, bg='yellow',
                                              command=self.start_timeout_team2)
        self.timeout_team2_button.place(x=816, y=375, anchor='center')

        self.timeout_label_team2 = None

        # Кнопка включения ТАБЛО
        self.on_tablo_button = tk.Button(self.master, text="ВКЛ. Табло", width=12, command=self.on_tablo)
        self.on_tablo_button.place(x=727, y=729, anchor='center')

        # Кнопка выключения ТАБЛО
        self.off_tablo_button = tk.Button(self.master, text="ВЫКЛ. Табло", width=12, command=self.off_tablo)
        self.off_tablo_button.place(x=834, y=729, anchor='center')
        self.off_tablo_button.config(state=tk.DISABLED)

        # Кнопка записать списки команд
        self.list_teams = tk.Button(self.master, text="ЗАПИСАТЬ СПИСКИ ИГРОКОВ", command=self.list_save_comands)
        self.list_teams.place(x=450, y=729, anchor='center')
        ####################

        self.cancel_flg = False

        ###################################################### КНОПКИ
        self.penalty_button = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply)
        self.penalty_button.place(x=276, y=464, anchor='center')

        self.penalty_button2 = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply2)
        self.penalty_button2.place(x=276, y=507, anchor='center')

        self.penalty_button3 = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply3)
        self.penalty_button3.place(x=276, y=550, anchor='center')

        self.penalty_button4 = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply4)
        self.penalty_button4.place(x=727, y=464, anchor='center')

        self.penalty_button5 = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply5)
        self.penalty_button5.place(x=727, y=507, anchor='center')

        self.penalty_button5 = tk.Button(self.master, text="ШТРАФ", width=11, command=self.penalty_apply6)
        self.penalty_button5.place(x=727, y=550, anchor='center')

        self.penalty_cancel_button = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty)
        self.penalty_cancel_button.place(x=384, y=464, anchor='center')

        self.penalty_cancel_button2 = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty2)
        self.penalty_cancel_button2.place(x=384, y=507, anchor='center')

        self.penalty_cancel_button3 = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty3)
        self.penalty_cancel_button3.place(x=384, y=550, anchor='center')

        self.penalty_cancel_button4 = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty4)
        self.penalty_cancel_button4.place(x=834, y=464, anchor='center')

        self.penalty_cancel_button5 = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty5)
        self.penalty_cancel_button5.place(x=834, y=507, anchor='center')

        self.penalty_cancel_button6 = tk.Button(self.master, text="ОТМЕНА", width=11, command=self.cancel_penalty6)
        self.penalty_cancel_button6.place(x=834, y=550, anchor='center')

        ###################################################### Нонец штрафных

        ########################### ГОЛ ЗАБИЛ ##########################
        self.number1_goal_label = tk.Label(self.master, text='НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number1_goal_label.place(x=38, y=639, anchor='center')

        self.goal_scored_number = ttk.Combobox(self.master, values=list(self.data_team.keys()), font=("Helvetica", 14),
                                               justify="center")
        self.goal_scored_number.place(x=83, y=639, anchor='center', width=50, height=25)

        self.goal_scored = tk.Button(self.master, text="ГОЛ ЗАБИЛ", width=11, command=self.goal)
        self.goal_scored.place(x=160, y=640, anchor='center')

        self.number_goal_label2 = tk.Label(self.master, text='НОМЕР', font=("Helvetica", 8), fg='black', bg='lightblue')
        self.number_goal_label2.place(x=709, y=639, anchor='center')

        self.goal_scored_number2 = ttk.Combobox(self.master, values=list(self.data_team2.keys()),
                                                font=("Helvetica", 14), justify="center")
        self.goal_scored_number2.place(x=754, y=639, anchor='center', width=50, height=25)

        self.goal_scored2 = tk.Button(self.master, text="ГОЛ ЗАБИЛ", width=11, command=self.goal2)
        self.goal_scored2.place(x=831, y=640, anchor='center')

        #######################################  ВВОД ДАННЫХ В ОКНЕ MASTER #####################################

        self.penalty_number_entry = ttk.Combobox(self.master, values=list(self.data_team.keys()),
                                                 font=("Helvetica", 14), justify="center")
        self.penalty_number_entry.place(x=102, y=462, anchor='center', width=50, height=25)

        self.penalty_minutes_entry = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry.insert(0, '2')
        self.penalty_minutes_entry.place(x=200, y=462, anchor='center', width=30, height=25)

        self.penalty_flg = False

        self.penalty_number_entry2 = ttk.Combobox(self.master, values=list(self.data_team.keys()),
                                                  font=("Helvetica", 14), justify="center")
        self.penalty_number_entry2.place(x=102, y=505, anchor='center', width=50, height=25)

        self.penalty_minutes_entry2 = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry2.insert(0, '2')
        self.penalty_minutes_entry2.place(x=200, y=505, anchor='center', width=30, height=25)

        self.penalty_flg2 = False

        self.penalty_number_entry3 = ttk.Combobox(self.master, values=list(self.data_team.keys()),
                                                  font=("Helvetica", 14), justify="center")
        self.penalty_number_entry3.place(x=102, y=548, anchor='center', width=50, height=25)

        self.penalty_minutes_entry3 = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry3.insert(0, '2')
        self.penalty_minutes_entry3.place(x=200, y=548, anchor='center', width=30, height=25)

        self.penalty_flg3 = False

        self.penalty_number_entry4 = ttk.Combobox(self.master, values=list(self.data_team2.keys()),
                                                  font=("Helvetica", 14), justify="center")
        self.penalty_number_entry4.place(x=552, y=462, anchor='center', width=50, height=25)

        self.penalty_minutes_entry4 = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry4.insert(0, '2')
        self.penalty_minutes_entry4.place(x=650, y=462, anchor='center', width=30, height=25)

        self.penalty_flg4 = False

        self.penalty_number_entry5 = ttk.Combobox(self.master, values=list(self.data_team2.keys()),
                                                  font=("Helvetica", 14), justify="center")
        self.penalty_number_entry5.place(x=552, y=505, anchor='center', width=50, height=25)

        self.penalty_minutes_entry5 = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry5.insert(0, '2')
        self.penalty_minutes_entry5.place(x=650, y=505, anchor='center', width=30, height=25)

        self.penalty_flg5 = False

        self.penalty_number_entry6 = ttk.Combobox(self.master, values=list(self.data_team2.keys()),
                                                  font=("Helvetica", 14), justify="center")
        self.penalty_number_entry6.place(x=552, y=548, anchor='center', width=50, height=25)

        self.penalty_minutes_entry6 = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.penalty_minutes_entry6.insert(0, '2')
        self.penalty_minutes_entry6.place(x=650, y=548, anchor='center', width=30, height=25)

        self.penalty_flg6 = False

        ################################################## СЕКУНДОМЕР

        # Создаем секундомер
        self.stopwatch = Stopwatch()
        self.general_timer = Stopwatch()

        # Создаем метку для отображения времени
        self.stopwatch_time_label = tk.Label(text="00:00", font=("DS-Digital", 30), bg='black', fg='yellow')
        self.stopwatch_time_label.place(relx=0.5, rely=0.055, anchor='center')

        self.time_text_label = tk.Label(self.master, text="СЕКУНДОМЕР", font=("Helvetica", 10), bg="black", fg="white")
        self.time_text_label.place(x=450, y=15, anchor="center")

        self.current_time = 0
        self.elapse_time = 20 * 60

        self.stopwatch_current_time = 0
        self.stopwatch_elapse_time = 1
        ################################################################

        ###########################################Горячие КЛАВИШИ  #######################################
        # self.master.bind("<space>", self.toggle_timer_space)
        self.master.bind("<Return>", self.toggle_timer_enter)

        ################# РАЗРАБОТЧИК #############################################################
        self.creator = tk.Label(self.master, text="Разработчик", font=("Arial", 7), fg="WHITE",bg='green', cursor="hand2")
        self.creator.place(x=852, y=750, anchor='center')

        self.creator.bind("<Button-1>", lambda e: self.show_info())

        # self.update_timer()

    def show_info(self):
        # Создание нового окна с информацией
        self.info_window = tk.Toplevel()
        self.info_window.title("Разработчик")
        self.info_window.geometry("300x100")
        self.info_window.resizable(False, False)
        self.info_window['bg'] = 'black'

        # Текст в новом окне
        self.label_info = tk.Label(self.info_window, text="Разработчик: Тен Владислав\n"
                                                          "По вопросам сотрудничества: +77017107829\n"
                                                          "e-mail: vladislav.ten1987@gmail.com", font=("Arial", 10), fg='white', bg='black')
        self.label_info.pack(expand=True)
    ##########################################  ФУНКЦИИ ###################################################

    ####################################### тест штрафных
    def general_start(self):
        self.toggle_timer()
        self.stopwatch_toggle_timer()
        self.penalty_update_timer()
        self.penalty_update_timer2()
        self.penalty_update_timer3()
        self.penalty_update_timer4()
        self.penalty_update_timer5()
        self.penalty_update_timer6()

    def penalty_apply(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry.get().strip() == '2'
                    or self.penalty_minutes_entry.get().strip() == '4'
                    or self.penalty_minutes_entry.get().strip() == '5'):
                if not self.penalty_number_entry.get().strip() == '':
                    if self.penalty_number_entry.get() in self.data_team:
                        self.penalty_timer_label.place_forget()
                        self.penalty_timer_label_control.place_forget()
                        self.penalty_number_label.place_forget()
                        self.penalty_number_label_control.place_forget()
                        self.penalty_minutes = self.penalty_minutes_entry.get().strip()
                        self.penalty_timer_label = tk.Label(self.timer_window, text=f"0{self.penalty_minutes}:00",
                                                            font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label.place(relx=0.26, rely=0.65, anchor="center")
                        self.penalty_timer_label_control = tk.Label(self.master, text=f"0{self.penalty_minutes}:00",
                                                                    font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label_control.place(x=230, y=188, anchor="center")
                        self.penalty_number = self.penalty_number_entry.get().strip()
                        self.penalty_number_label = tk.Label(self.timer_window, text=self.penalty_number,
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label.place(relx=0.1, rely=0.65, anchor="center")
                        self.penalty_number_label_control = tk.Label(self.master, text=self.penalty_number,
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label_control.place(x=189, y=188, anchor="center")
                        self.penalty_timer.reset()
                        self.penalty_flg = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry.get().strip()} отсутствует в списке игроков хозяев")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply2(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry2.get().strip() == '2'
                    or self.penalty_minutes_entry2.get().strip() == '4'
                    or self.penalty_minutes_entry2.get().strip() == '5'):
                if not self.penalty_number_entry2.get().strip() == '':
                    if self.penalty_number_entry2.get() in self.data_team:
                        self.penalty_timer_label2.place_forget()
                        self.penalty_number_label2.place_forget()
                        self.penalty_timer_label2_control.place_forget()
                        self.penalty_number_label2_control.place_forget()
                        self.penalty_minutes2 = self.penalty_minutes_entry2.get().strip()
                        self.penalty_timer_label2 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes2}:00",
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label2.place(relx=0.26, rely=0.74, anchor="center")
                        self.penalty_timer_label2_control = tk.Label(self.master, text=f"0{self.penalty_minutes2}:00",
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label2_control.place(x=230, y=214, anchor="center")

                        self.penalty_number2 = self.penalty_number_entry2.get().strip()
                        self.penalty_number_label2 = tk.Label(self.timer_window, text=self.penalty_number2,
                                                              font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label2.place(relx=0.1, rely=0.74, anchor="center")

                        self.penalty_number_label2_control = tk.Label(self.master, text=self.penalty_number2,
                                                                      font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label2_control.place(x=188, y=214, anchor="center")
                        self.penalty_timer2.reset()
                        self.penalty_flg2 = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry2.get().strip()} отсутствует в списке игроков хозяев")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply3(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry3.get().strip() == '2'
                    or self.penalty_minutes_entry3.get().strip() == '4'
                    or self.penalty_minutes_entry3.get().strip() == '5'):
                if not self.penalty_number_entry3.get() == '':
                    if self.penalty_number_entry3.get() in self.data_team:
                        self.penalty_timer_label3.place_forget()
                        self.penalty_timer_label3_control.place_forget()
                        self.penalty_number_label3.place_forget()
                        self.penalty_number_label3_control.place_forget()
                        self.penalty_minutes3 = self.penalty_minutes_entry3.get().strip()
                        self.penalty_timer_label3 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes3}:00",
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label3.place(relx=0.26, rely=0.83, anchor="center")
                        self.penalty_timer_label3_control = tk.Label(self.master, text=f"0{self.penalty_minutes3}:00",
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label3_control.place(x=230, y=239, anchor="center")
                        self.penalty_number3 = self.penalty_number_entry3.get().strip()
                        self.penalty_number_label3 = tk.Label(self.timer_window, text=self.penalty_number3,
                                                              font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label3.place(relx=0.1, rely=0.83, anchor="center")
                        self.penalty_number_label3_control = tk.Label(self.master, text=self.penalty_number3,
                                                                      font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label3_control.place(x=188, y=239, anchor="center")
                        self.penalty_timer3.reset()
                        self.penalty_flg3 = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry3.get().strip()} отсутствует в списке игроков хозяев")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply4(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry4.get().strip() == '2'
                    or self.penalty_minutes_entry4.get() == '4'
                    or self.penalty_minutes_entry4.get() == '5'):
                if not self.penalty_number_entry4.get() == '':
                    if self.penalty_number_entry4.get() in self.data_team2:
                        self.penalty_timer_label4.place_forget()
                        self.penalty_timer_label4_control.place_forget()
                        self.penalty_number_label4.place_forget()
                        self.penalty_number_label4_control.place_forget()
                        self.penalty_minutes4 = self.penalty_minutes_entry4.get().strip()
                        self.penalty_timer_label4 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes4}:00",
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label4.place(relx=0.86, rely=0.65, anchor="center")
                        self.penalty_timer_label4_control = tk.Label(self.master, text=f"0{self.penalty_minutes4}:00",
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label4_control.place(x=688, y=189, anchor="center")
                        self.penalty_number4 = self.penalty_number_entry4.get().strip()
                        self.penalty_number_label4 = tk.Label(self.timer_window, text=self.penalty_number4,
                                                              font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label4.place(relx=0.7, rely=0.65, anchor="center")
                        self.penalty_number_label4_control = tk.Label(self.master, text=self.penalty_number4,
                                                                      font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label4_control.place(x=646, y=189, anchor="center")
                        self.penalty_timer4.reset()
                        self.penalty_flg4 = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry4.get().strip()} отсутствует в списке игроков гостей")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply5(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry5.get().strip() == '2'
                    or self.penalty_minutes_entry5.get().strip() == '4'
                    or self.penalty_minutes_entry5.get().strip() == '5'):
                if not self.penalty_number_entry5.get().strip() == '':
                    if self.penalty_number_entry5.get() in self.data_team2:
                        self.penalty_timer_label5.place_forget()
                        self.penalty_timer_label5_control.place_forget()
                        self.penalty_number_label5.place_forget()
                        self.penalty_number_label5_control.place_forget()
                        self.penalty_minutes5 = self.penalty_minutes_entry5.get().strip()
                        self.penalty_timer_label5 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes5}:00",
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label5.place(relx=0.86, rely=0.74, anchor="center")
                        self.penalty_timer_label5_control = tk.Label(self.master, text=f"0{self.penalty_minutes5}:00",
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label5_control.place(x=688, y=214, anchor="center")
                        self.penalty_number5 = self.penalty_number_entry5.get().strip()
                        self.penalty_number_label5 = tk.Label(self.timer_window, text=self.penalty_number5,
                                                              font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label5.place(relx=0.7, rely=0.74, anchor="center")
                        self.penalty_number_label5_control = tk.Label(self.master, text=self.penalty_number5,
                                                                      font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label5_control.place(x=646, y=214, anchor="center")
                        self.penalty_timer5.reset()
                        self.penalty_flg5 = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry5.get().strip()} отсутствует в списке игроков гостей")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_apply6(self):
        if not self.timer_running:
            if (self.penalty_minutes_entry6.get().strip() == '2'
                    or self.penalty_minutes_entry6.get().strip() == '4'
                    or self.penalty_minutes_entry6.get().strip() == '5'):
                if not self.penalty_number_entry6.get().strip() == '':
                    if self.penalty_number_entry6.get() in self.data_team2:
                        self.penalty_timer_label6.place_forget()
                        self.penalty_timer_label6_control.place_forget()
                        self.penalty_number_label6.place_forget()
                        self.penalty_number_label6_control.place_forget()
                        self.penalty_minutes6 = self.penalty_minutes_entry6.get().strip()
                        self.penalty_timer_label6 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes6}:00",
                                                             font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_timer_label6.place(relx=0.86, rely=0.83, anchor="center")
                        self.penalty_timer_label6_control = tk.Label(self.master, text=f"0{self.penalty_minutes6}:00",
                                                                     font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_timer_label6_control.place(x=688, y=239, anchor="center")
                        self.penalty_number6 = self.penalty_number_entry6.get().strip()
                        self.penalty_number_label6 = tk.Label(self.timer_window, text=self.penalty_number6,
                                                              font=("DS-Digital", 50), bg="black", fg="yellow")
                        self.penalty_number_label6.place(relx=0.7, rely=0.83, anchor="center")
                        self.penalty_number_label6_control = tk.Label(self.master, text=self.penalty_number6,
                                                                      font=("DS-Digital", 16), bg="black", fg="yellow")
                        self.penalty_number_label6_control.place(x=646, y=239, anchor="center")
                        self.penalty_timer6.reset()
                        self.penalty_flg6 = True
                    else:
                        messagebox.showinfo("Информация",
                                            f"Номер: {self.penalty_number_entry6.get().strip()} отсутствует в списке игроков гостей")
                else:
                    messagebox.showinfo("Информация", "Введите номер игрока")

            else:
                messagebox.showinfo("Информация", "Не корректно введены данные\nВведите 2, 4 или 5 минут")

        else:
            messagebox.showinfo("Информация", "Нельзя записать данные о штрафе, пока идет таймер")

    def penalty_update_timer(self):
        if self.timer_running and self.penalty_flg:
            self.penalty_timer.start()
            penalty_current_time = int(self.penalty_minutes) * 60 - self.penalty_timer.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label.config(text=string)
            self.penalty_timer_label_control.config(text=string)
            self.master.after(10, self.penalty_update_timer)
        else:
            self.penalty_timer.stop()

    def penalty_update_timer2(self):
        if self.timer_running and self.penalty_flg2:
            self.penalty_timer2.start()
            penalty_current_time = int(self.penalty_minutes2) * 60 - self.penalty_timer2.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty2()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label2.config(text=string)
            self.penalty_timer_label2_control.config(text=string)
            self.master.after(10, self.penalty_update_timer2)
        else:
            self.penalty_timer2.stop()

    def penalty_update_timer3(self):
        if self.timer_running and self.penalty_flg3:
            self.penalty_timer3.start()
            penalty_current_time = int(self.penalty_minutes3) * 60 - self.penalty_timer3.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty3()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label3.config(text=string)
            self.penalty_timer_label3_control.config(text=string)
            self.master.after(10, self.penalty_update_timer3)
        else:
            self.penalty_timer3.stop()

    def penalty_update_timer4(self):
        if self.timer_running and self.penalty_flg4:
            self.penalty_timer4.start()
            penalty_current_time = int(self.penalty_minutes4) * 60 - self.penalty_timer4.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty4()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label4.config(text=string)
            self.penalty_timer_label4_control.config(text=string)
            self.master.after(10, self.penalty_update_timer4)
        else:
            self.penalty_timer4.stop()

    def penalty_update_timer5(self):
        if self.timer_running and self.penalty_flg5:
            self.penalty_timer5.start()
            penalty_current_time = int(self.penalty_minutes5) * 60 - self.penalty_timer5.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty5()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label5.config(text=string)
            self.penalty_timer_label5_control.config(text=string)
            self.master.after(10, self.penalty_update_timer5)
        else:
            self.penalty_timer5.stop()

    def penalty_update_timer6(self):
        if self.timer_running and self.penalty_flg6:
            self.penalty_timer6.start()
            penalty_current_time = int(self.penalty_minutes6) * 60 - self.penalty_timer6.elapsed
            if penalty_current_time <= 1:
                self.cancel_penalty6()
            minutes = int(penalty_current_time // 60)
            seconds = int(penalty_current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.penalty_timer_label6.config(text=string)
            self.penalty_timer_label6_control.config(text=string)
            self.master.after(10, self.penalty_update_timer6)
        else:
            self.penalty_timer6.stop()

    def cancel_penalty(self):
        self.penalty_flg = False
        self.penalty_timer_label.place_forget()
        self.penalty_timer_label_control.place_forget()
        self.penalty_number_label.place_forget()
        self.penalty_number_label_control.place_forget()

    def cancel_penalty2(self):
        self.penalty_flg2 = False
        self.penalty_timer_label2.place_forget()
        self.penalty_timer_label2_control.place_forget()
        self.penalty_number_label2.place_forget()
        self.penalty_number_label2_control.place_forget()

    def cancel_penalty3(self):
        self.penalty_flg3 = False
        self.penalty_timer_label3.place_forget()
        self.penalty_timer_label3_control.place_forget()
        self.penalty_number_label3.place_forget()
        (self.penalty_number_label3_control.place_forget())

    def cancel_penalty4(self):
        self.penalty_flg4 = False
        self.penalty_timer_label4.place_forget()
        self.penalty_timer_label4_control.place_forget()
        self.penalty_number_label4.place_forget()
        self.penalty_number_label4_control.place_forget()

    def cancel_penalty5(self):
        self.penalty_flg5 = False
        self.penalty_timer_label5.place_forget()
        self.penalty_timer_label5_control.place_forget()
        self.penalty_number_label5.place_forget()
        self.penalty_number_label5_control.place_forget()

    def cancel_penalty6(self):
        self.penalty_flg6 = False
        self.penalty_timer_label6.place_forget()
        self.penalty_timer_label6_control.place_forget()
        self.penalty_number_label6.place_forget()
        self.penalty_number_label6_control.place_forget()

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
        self.timeout_team1_label_control.config(text="00:00")
        self.timeout_team1_button.config(state=tk.DISABLED)

        self.timeout_label_team1 = tk.Label(self.timer_window, text="ТАЙМАУТ", font=("Helvetika", 16), bg="black",
                                            fg="white")
        self.timeout_label_team1.place(relx=0.2, rely=0.44, anchor="center")
        self.timeout_label_team1_control = tk.Label(self.master, text="ТАЙМАУТ", font=("Helvetika", 6), bg="black",
                                                    fg="white")
        self.timeout_label_team1_control.place(x=215, y=125, anchor="center")

        self.countdown_team1(1 * 30)

    def countdown_team1(self, remaining_time):
        if remaining_time <= 0:
            self.timeout_team1_label.config(text="")
            self.timeout_team1_label_control.config(text="")
            self.timeout_team1_button.config(state=tk.NORMAL)
            if self.timeout_label_team1:
                self.timeout_label_team1.place_forget()
                self.timeout_label_team1_control.place_forget()
                self.timeout_label_team1 = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.timeout_team1_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.timeout_team1_label_control.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.master.after(1000, self.countdown_team1, remaining_time - 1)

    # Таймаут функция team2
    def start_timeout_team2(self):
        self.timeout_team2_label.config(text="00:00")
        self.timeout_team2_label_control.config(text="00:00")
        self.timeout_team2_button.config(state=tk.DISABLED)

        self.timeout_label_team2 = tk.Label(self.timer_window, text="ТАЙМАУТ", font=("Helvetika", 16), bg="black",
                                            fg="white")
        self.timeout_label_team2.place(relx=0.8, rely=0.44, anchor="center")
        self.timeout_label_team2_control = tk.Label(self.master, text="ТАЙМАУТ", font=("Helvetika", 6), bg="black",
                                                    fg="white")
        self.timeout_label_team2_control.place(x=674, y=125, anchor="center")

        self.countdown_team2(1 * 30)

    def countdown_team2(self, remaining_time):
        if remaining_time <= 0:
            self.timeout_team2_label.config(text="")
            self.timeout_team2_label_control.config(text="")
            self.timeout_team2_button.config(state=tk.NORMAL)
            if self.timeout_label_team2:
                self.timeout_label_team2.place_forget()
                self.timeout_label_team2_control.place_forget()
                self.timeout_label_team2 = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.timeout_team2_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.timeout_team2_label_control.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.master.after(1000, self.countdown_team2, remaining_time - 1)

    ############# КОНЕЦ функции таймаут

    # Таймер перерыва 17 минут
    def start_break_timer(self):
        self.break_time.config(text="00:00")
        self.break_time_control.config(text="00:00")
        self.button_break.config(state=tk.DISABLED)

        self.break_label = tk.Label(self.timer_window, text="ПЕРЕРЫВ", font=("Helvetica", 25), bg="black", fg="white")
        self.break_label.place(relx=0.5, rely=0.80, anchor="center")
        self.break_label_control = tk.Label(self.master, text="ПЕРЕРЫВ", font=("Helvetica", 10), bg="black", fg="white")
        self.break_label_control.place(x=450, y=223, anchor="center")

        self.countdown_break(17 * 60)  # Установка времени перерыва, пример: 17 * 60 = 17 минут

    def countdown_break(self, remaining_time):
        if remaining_time <= 0 or self.cancel_flg == True:
            self.break_time.config(text="")
            self.break_time_control.config(text="")
            self.button_break.config(state=tk.NORMAL)
            self.cancel_flg = False

            if self.break_label:
                self.break_label.place_forget()
                self.break_label_control.place_forget()
                self.break_label = None
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.break_time.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.break_time_control.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.timer_window.after(1000, self.countdown_break, remaining_time - 1)

    def cancel_break_timer(self):
        self.cancel_flg = True

    ###############  КОНЕЦ Таймер перерыва 17 минут

    def toggle_timer_enter(self, event):
        self.save_teams()

    def reset_timer(self):
        self.timer_running = False
        self.general_timer.reset()
        self.stopwatch.reset()
        self.elapse_time = 20 * 60
        self.stopwatch_elapse_time = 1
        self.button.config(text="ИГРА")
        self.timer_label.config(text='20:00')
        self.timer_label_control.config(text='20:00')
        self.stopwatch_time_label.config(text='00:00')
        self.reset_button.config(state=tk.NORMAL)

    def save_teams(self):
        if not self.timer_running:
            team1_name = self.team1_name_entry.get().strip()
            team2_name = self.team2_name_entry.get().strip()
            self.team1_label.config(text=team1_name.upper())
            self.team1_label_control.config(text=team1_name.upper())
            self.team2_label.config(text=team2_name.upper())
            self.team2_label_control.config(text=team2_name.upper())



    def goal_home_increase(self):
        if not self.timer_running:
            self.goal_home_var.set(self.goal_home_var.get() + 1)

    def goal_home_decrease(self):
        if not self.timer_running:
            self.goal_home_var.set(max(0, self.goal_home_var.get() - 1))

    def period_increase(self):
        if not self.timer_running:
            self.period_var.set(self.period_var.get() + 1)
            self.start_break_timer()

    def period_decrease(self):
        if not self.timer_running:
            self.period_var.set(max(1, self.period_var.get() - 1))
            # self.cancel_break_timer()

    def goal_away_increase(self):
        if not self.timer_running:
            self.goal_away_var.set(self.goal_away_var.get() + 1)

    def goal_away_decrease(self):
        if not self.timer_running:
            self.goal_away_var.set(max(0, self.goal_away_var.get() - 1))

    def add_minute(self):
        if not self.timer_running:
            self.elapse_time += 60
            self.stopwatch_elapse_time -= 60
            self.current_time = self.elapse_time - self.general_timer.elapsed
            minutes = int(self.current_time // 60)
            seconds = int(self.current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=string)
            self.timer_label_control.config(text=string)

            self.stopwatch_current_time = self.stopwatch.elapsed + self.stopwatch_elapse_time
            stopwatch_minutes = int(self.stopwatch_current_time // 60)
            stopwatch_seconds = int(self.stopwatch_current_time % 60)
            stopwatch_time_string = f"{stopwatch_minutes:02d}:{stopwatch_seconds:02d}"
            self.stopwatch_time_label.config(text=stopwatch_time_string)

    def subtract_minute(self):
        if not self.timer_running:
            self.elapse_time -= 60
            self.stopwatch_elapse_time += 60
            self.current_time = self.elapse_time - self.general_timer.elapsed
            minutes = int(self.current_time // 60)
            seconds = int(self.current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=string)
            self.timer_label_control.config(text=string)

            self.stopwatch_current_time = self.stopwatch.elapsed + self.stopwatch_elapse_time
            stopwatch_minutes = int(self.stopwatch_current_time // 60)
            stopwatch_seconds = int(self.stopwatch_current_time % 60)
            stopwatch_time_string = f"{stopwatch_minutes:02d}:{stopwatch_seconds:02d}"
            self.stopwatch_time_label.config(text=stopwatch_time_string)

    def add_second(self):
        if not self.timer_running:
            self.elapse_time += 1
            self.stopwatch_elapse_time -= 1
            self.current_time = self.elapse_time - self.general_timer.elapsed
            minutes = int(self.current_time // 60)
            seconds = int(self.current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=string)
            self.timer_label_control.config(text=string)

            self.stopwatch_current_time = self.stopwatch.elapsed + self.stopwatch_elapse_time
            stopwatch_minutes = int(self.stopwatch_current_time // 60)
            stopwatch_seconds = int(self.stopwatch_current_time % 60)
            stopwatch_time_string = f"{stopwatch_minutes:02d}:{stopwatch_seconds:02d}"
            self.stopwatch_time_label.config(text=stopwatch_time_string)

    def subtract_second(self):
        if not self.timer_running:
            self.elapse_time -= 1
            self.stopwatch_elapse_time += 1
            self.current_time = self.elapse_time - self.general_timer.elapsed
            minutes = int(self.current_time // 60)
            seconds = int(self.current_time % 60)
            string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=string)
            self.timer_label_control.config(text=string)

            self.stopwatch_current_time = self.stopwatch.elapsed + self.stopwatch_elapse_time
            stopwatch_minutes = int(self.stopwatch_current_time // 60)
            stopwatch_seconds = int(self.stopwatch_current_time % 60)
            stopwatch_time_string = f"{stopwatch_minutes:02d}:{stopwatch_seconds:02d}"
            self.stopwatch_time_label.config(text=stopwatch_time_string)

    def stopwatch_toggle_timer(self):
        if self.timer_running:
            self.stopwatch.start()
            self.stopwatch_update_time()

    def stopwatch_update_time(self):
        if self.timer_running:
            # Получаем текущее время с секундомера
            self.stopwatch_current_time = self.stopwatch.elapsed + self.stopwatch_elapse_time
            # Преобразуем секунды в минуты и секунды
            stopwatch_minutes = int(self.stopwatch_current_time // 60)
            stopwatch_seconds = int(self.stopwatch_current_time % 60)
            # Форматируем время
            stopwatch_time_string = f"{stopwatch_minutes:02d}:{stopwatch_seconds:02d}"
            # Обновляем текст на метке
            self.stopwatch_time_label.config(text=stopwatch_time_string)
            # Запускаем обновление снова через 100 мс
            self.master.after(10, self.stopwatch_update_time)
        else:
            self.stopwatch.stop()

    def toggle_timer(self):
        if self.timer_running:
            self.reset_button.config(state=tk.NORMAL)
            self.timer_running = False
            self.button.config(text="ИГРА", bg="lightgreen", fg="black")


        else:
            self.general_timer.start()
            self.timer_running = True
            self.update_timer()
            self.reset_button.config(state=tk.DISABLED)
            self.button.config(text="ПАУЗА", bg="red", fg="white")

    def update_timer(self):
        if self.timer_running:
            self.current_time = self.elapse_time - self.general_timer.elapsed
            self.current_time = self.elapse_time - self.general_timer.elapsed
            minutes = int(self.current_time // 60)
            seconds = int(self.current_time % 60)
            stopwatch_time_string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=stopwatch_time_string)
            self.timer_label_control.config(text=stopwatch_time_string)
            self.master.after(10, self.update_timer)
            if self.current_time <= 1:
                self.play_sound()
                self.red_line_left = tk.Frame(self.master, bg='red', width=10, height=2000)
                self.red_line_left.pack(side='left')
                self.red_line_right = tk.Frame(self.master, bg='red', width=10, height=2000)
                self.red_line_right.pack(side='right')
                self.red_line_top = tk.Frame(self.master, bg='red', width=2000, height=10)
                self.red_line_top.pack(side='top')
                self.red_line_bottom = tk.Frame(self.master, bg='red', width=2000, height=10)
                self.red_line_bottom.pack(side='bottom')

                self.red_line_left2 = tk.Frame(self.timer_window, bg='red', width=10, height=2000)
                self.red_line_left2.pack(side='left')
                self.red_line_right2 = tk.Frame(self.timer_window, bg='red', width=10, height=2000)
                self.red_line_right2.pack(side='right')
                self.red_line_top2 = tk.Frame(self.timer_window, bg='red', width=2000, height=10)
                self.red_line_top2.pack(side='top')
                self.red_line_bottom2 = tk.Frame(self.timer_window, bg='red', width=2000, height=10)
                self.red_line_bottom2.pack(side='bottom')

                self.reset_timer()
                self.timer_label.config(text='00:00')
                self.timer_label_control.config(text='00:00')
                self.stopwatch_time_label.config(text='20:00')
                self.master.after(8000, self.remove_red_line)

                # self.master.after(3000, self.end_time())

        else:
            self.general_timer.stop()

    def remove_red_line(self):
        self.red_line_left.destroy()
        self.red_line_right.destroy()
        self.red_line_top.destroy()
        self.red_line_bottom.destroy()

        self.red_line_left2.destroy()
        self.red_line_right2.destroy()
        self.red_line_top2.destroy()
        self.red_line_bottom2.destroy()


    def end_time(self):
        self.red_line_left.forget()
        self.red_line_right.forget()
        self.red_line_top.forget()
        self.red_line_bottom.forget()

    ############################# ЗАПИСЬ КОМАНД ################################################
    #### ЧИТАЕМ списки команд из файла data_team.pkl

    def list_save_comands(self):
        def save1():
            if self.player_number_entry.get().isdigit() and self.player_name_entry.get() != '':
                self.data_team[self.player_number_entry.get()] = self.player_name_entry.get().upper()
                with open("data_team_home.pkl", "wb") as f:
                    pickle.dump(self.data_team, f)

                self.show_players()
                self.update_combo_box()

            else:
                messagebox.showinfo('Ошибка', 'Введите корректные данные')


        def save2():
            if self.player_number_entry2.get().isdigit() and self.player_name_entry2.get() != '':
                self.data_team2[self.player_number_entry2.get()] = self.player_name_entry2.get().upper()
                with open("data_team_guest.pkl", "wb") as f:
                    pickle.dump(self.data_team2, f)

                self.show_players2()
                self.update_combo_box()
            else:
                messagebox.showinfo('Ошибка', 'Введите корректные данные')

        def clear_data():
            self.data_team = {}
            with open("data_team_home.pkl", "wb") as f:
                pickle.dump(self.data_team, f)
            self.update_combo_box()

        def clear_data2():
            self.data_team2 = {}
            with open("data_team_guest.pkl", "wb") as f:
                pickle.dump(self.data_team2, f)
            self.update_combo_box()

        self.save_comands_window = tk.Toplevel(root)
        self.save_comands_window.title("ЗАПИСЬ ИГРОКОВ")
        self.save_comands_window.geometry('600x490')
        self.save_comands_window['bg'] = 'lightblue'

        self.text_box_home = tk.Text(self.save_comands_window, height=15, width=34)
        self.text_box_home.place(relx=0.25, y=315, anchor='center')

        self.text_box_guests = tk.Text(self.save_comands_window, height=15, width=34)
        self.text_box_guests.place(relx=0.75, y=315, anchor='center')
        #### ДЕКОРАЦИИИ ############
        white_strip = tk.Frame(self.save_comands_window, bg="white", width=600, height=1)
        white_strip.place(x=0, y=35)
        white_strip = tk.Frame(self.save_comands_window, bg="white", width=1, height=490)
        white_strip.place(x=300, y=0)

        team1_label = tk.Label(self.save_comands_window, text='КОМАНДА ХОЗЯЕВ', font=("Helvetica", 10), fg='black',
                               bg='lightblue')
        team1_label.place(x=150, y=19, anchor='center')
        team2_label = tk.Label(self.save_comands_window, text='КОМАНДА ГОСТЕЙ', font=("Helvetica", 10), fg='black',
                               bg='lightblue')
        team2_label.place(x=450, y=19, anchor='center')

        number_team1_label = tk.Label(self.save_comands_window, text='Номер', font=("Helvetica", 10), fg='black',
                                      bg='lightblue')
        number_team1_label.place(x=43, y=58, anchor='center')
        number_team2_label = tk.Label(self.save_comands_window, text='Номер', font=("Helvetica", 10), fg='black',
                                      bg='lightblue')
        number_team2_label.place(x=345, y=58, anchor='center')

        fio_team1_label = tk.Label(self.save_comands_window, text='Имя/Фамилия', font=("Helvetica", 10), fg='black',
                                   bg='lightblue')
        fio_team1_label.place(x=184, y=58, anchor='center')
        fio_team2_label = tk.Label(self.save_comands_window, text='Имя/Фамилия', font=("Helvetica", 10), fg='black',
                                   bg='lightblue')
        fio_team2_label.place(x=484, y=58, anchor='center')

        self.player_number_entry = tk.Entry(self.save_comands_window, font=("Helvetica", 12), justify="center")
        self.player_number_entry.place(x=45, y=84, anchor='center', width=30, height=25)
        self.player_name_entry = tk.Entry(self.save_comands_window, font=("Helvetica", 12), justify="center")
        self.player_name_entry.place(x=184, y=84, anchor='center', width=180, height=25)
        self.save_button = tk.Button(self.save_comands_window, text="СОХРАНИТЬ", command=save1)
        self.save_button.place(x=152, y=123, anchor='center', width=244)

        self.player_number_entry2 = tk.Entry(self.save_comands_window, font=("Helvetica", 12), justify="center")
        self.player_number_entry2.place(x=345, y=84, anchor='center', width=30, height=25)
        self.player_name_entry2 = tk.Entry(self.save_comands_window, font=("Helvetica", 12), justify="center")
        self.player_name_entry2.place(x=484, y=84, anchor='center', width=180, height=25, )
        self.save_button2 = tk.Button(self.save_comands_window, text="СОХРАНИТЬ", command=save2)
        self.save_button2.place(x=453, y=123, anchor='center', width=244)

        show_team1_button = tk.Button(self.save_comands_window, text="ПОКАЗАТЬ ИГРОКОВ", command=self.show_players)
        show_team1_button.place(x=152, y=159, anchor='center', width=244)

        show_team2_button = tk.Button(self.save_comands_window, text="ПОКАЗАТЬ ИГРОКОВ", command=self.show_players2)
        show_team2_button.place(x=452, y=159, anchor='center', width=244)

        clear_data_button = tk.Button(self.save_comands_window, text="СТЕРЕТЬ СПИСОК", command=clear_data, bg='red',
                                      fg='white')
        clear_data_button.place(x=152, y=463, anchor='center', width=244)

        clear_data_button2 = tk.Button(self.save_comands_window, text="СТЕРЕТЬ СПИСОК", command=clear_data2, bg='red',
                                       fg='white')
        clear_data_button2.place(x=452, y=463, anchor='center', width=244)

    def goal(self):
        if self.goal_scored_number.get() in self.data_team and os.path.exists(
                f'photo_home/{self.goal_scored_number.get()}.jpg'):
            window_goal = tk.Toplevel(self.master)
            # window_goal.geometry('1280x1024')
            # window_goal.geometry('1280x1024')

            window_goal.title('ГОЛ')
            window_goal['bg'] = 'black'
            window_goal.geometry(
                f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
            window_goal['bg'] = 'black'
            window_goal.overrideredirect(True)
            window_goal.attributes('-topmost')

            image_path = f'photo_home/{self.goal_scored_number.get()}.jpg'
            image = Image.open(image_path)

            width, height = image.size
            # Вычисление нового размера изображения
            new_height = 400
            new_width = int(width * (new_height / height))

            image = image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            photo_label = tk.Label(window_goal, image=photo)
            photo_label.image = photo  # сохраняем ссылку на изображение, чтобы избежать сборщика мусора
            photo_label.place(relx=0.5, rely=0.44, anchor='center')

            number1 = self.goal_scored_number.get()
            name1 = self.data_team[number1]

            top_goal_label = tk.Label(window_goal, text='ГОЛ ЗАБИЛ', font=('Helvetica', 30, 'bold'), fg='white',
                                      bg='black')
            top_goal_label.place(relx=0.5, rely=0.12, anchor='center')

            plashka_label = tk.Frame(window_goal, width=130, height=120, bg='green')
            plashka_label.place(relx=0.5, rely=0.8, anchor='center')

            bottom_number_label = tk.Label(window_goal, text='НОМЕР', justify='center',
                                           font=("Helvetica", 23, 'bold'), bg="black", fg="white")
            bottom_number_label.place(relx=0.5, rely=0.72, anchor='center')

            goal_home_number = tk.Label(window_goal, text=f'{number1}', justify='center',
                                        font=("Helvetica", 69, 'bold'), bg="green", fg="white")
            goal_home_number.place(relx=0.5, rely=0.8, anchor='center')
            goal_home_name = tk.Label(window_goal, text=f'{name1}', justify='center',
                                      font=("Helvetica", 42, 'bold'), bg="black", fg="white")
            goal_home_name.place(relx=0.5, rely=0.9, anchor='center')

            window_goal.after(10000, window_goal.destroy)
        elif self.goal_scored_number.get() in self.data_team:
            window_goal = tk.Toplevel(self.master)
            window_goal.title('ГОЛ')
            window_goal['bg'] = 'black'
            window_goal.geometry(
                f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
            window_goal['bg'] = 'black'
            window_goal.overrideredirect(True)

            number1 = self.goal_scored_number.get()
            name1 = self.data_team[number1]

            top_goal_label = tk.Label(window_goal, text='ГОЛ ЗАБИЛ', font=('Helvetica', 30, 'bold'), fg='white',
                                      bg='black')
            top_goal_label.place(relx=0.5, rely=0.12, anchor='center')

            plashka_label = tk.Frame(window_goal, width=130, height=120, bg='green')
            plashka_label.place(relx=0.5, rely=0.5, anchor='center')

            bottom_number_label = tk.Label(window_goal, text='НОМЕР', justify='center',
                                           font=("Helvetica", 23, 'bold'), bg="black", fg="white")
            bottom_number_label.place(relx=0.5, rely=0.42, anchor='center')

            goal_guests_number = tk.Label(window_goal, text=f'{number1}', justify='center',
                                          font=("Helvetica", 69, 'bold'), bg="green", fg="white")
            goal_guests_number.place(relx=0.5, rely=0.5, anchor='center')
            goal_guests_name = tk.Label(window_goal, text=f'{name1}', justify='center',
                                        font=("Helvetica", 42, 'bold'), bg="black", fg="white")
            goal_guests_name.place(relx=0.5, rely=0.6, anchor='center')
            window_goal.after(10000, window_goal.destroy)

        else:
            messagebox.showinfo('Ошибка', 'Такого номера нет в списках игроков')

    def goal2(self):
        if self.goal_scored_number2.get() in self.data_team2 and os.path.exists(
                f'photo_guests/{self.goal_scored_number2.get()}.jpg'):
            window_goal = tk.Toplevel(self.master)
            # window_goal.geometry('1280x1024')
            window_goal.title('ГОЛ')
            window_goal['bg'] = 'black'
            window_goal.geometry(
                f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
            window_goal['bg'] = 'black'
            window_goal.overrideredirect(True)
            window_goal.attributes('-topmost')

            image_path = f'photo_guests/{self.goal_scored_number2.get()}.jpg'
            image = Image.open(image_path)
            width, height = image.size
            # Вычисление нового размера изображения
            new_height = 400
            new_width = int(width * (new_height / height))
            image = image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            photo_label = tk.Label(window_goal, image=photo)
            photo_label.image = photo  # сохраняем ссылку на изображение, чтобы избежать сборщика мусора
            photo_label.place(relx=0.5, rely=0.44, anchor='center')

            number2 = self.goal_scored_number2.get()
            name2 = self.data_team2[number2]

            top_goal_label = tk.Label(window_goal, text='ГОЛ ЗАБИЛ', font=('Helvetica', 30, 'bold'), fg='white',
                                      bg='black')
            top_goal_label.place(relx=0.5, rely=0.12, anchor='center')

            plashka_label = tk.Frame(window_goal, width=130, height=120, bg='white')
            plashka_label.place(relx=0.5, rely=0.8, anchor='center')

            bottom_number_label = tk.Label(window_goal, text='НОМЕР', justify='center',
                                           font=("Helvetica", 23, 'bold'), bg="black", fg="white")
            bottom_number_label.place(relx=0.5, rely=0.72, anchor='center')

            goal_guests_number = tk.Label(window_goal, text=f'{number2}', justify='center',
                                          font=("Helvetica", 69, 'bold'), bg="white", fg="black")
            goal_guests_number.place(relx=0.5, rely=0.8, anchor='center')
            goal_guests_name = tk.Label(window_goal, text=f'{name2}', justify='center',
                                        font=("Helvetica", 42, 'bold'), bg="black", fg="white")
            goal_guests_name.place(relx=0.5, rely=0.9, anchor='center')
            window_goal.after(10000, window_goal.destroy)
        elif self.goal_scored_number2.get() in self.data_team2:
            window_goal = tk.Toplevel(self.master)
            window_goal.title('ГОЛ')
            window_goal['bg'] = 'black'
            window_goal.geometry(
                f"{self.secondary_monitor.width}x{self.secondary_monitor.height}+{self.secondary_monitor.x}+{self.secondary_monitor.y}")
            window_goal['bg'] = 'black'
            window_goal.overrideredirect(True)

            number2 = self.goal_scored_number2.get()
            name2 = self.data_team2[number2]

            top_goal_label = tk.Label(window_goal, text='ГОЛ ЗАБИЛ', font=('Helvetica', 30, 'bold'), fg='white',
                                      bg='black')
            top_goal_label.place(relx=0.5, rely=0.12, anchor='center')

            plashka_label = tk.Frame(window_goal, width=130, height=120, bg='white')
            plashka_label.place(relx=0.5, rely=0.5, anchor='center')

            bottom_number_label = tk.Label(window_goal, text='НОМЕР', justify='center',
                                           font=("Helvetica", 23, 'bold'), bg="black", fg="white")
            bottom_number_label.place(relx=0.5, rely=0.42, anchor='center')

            goal_guests_number = tk.Label(window_goal, text=f'{number2}', justify='center',
                                          font=("Helvetica", 69, 'bold'), bg="white", fg="black")
            goal_guests_number.place(relx=0.5, rely=0.5, anchor='center')
            goal_guests_name = tk.Label(window_goal, text=f'{name2}', justify='center',
                                        font=("Helvetica", 42, 'bold'), bg="black", fg="white")
            goal_guests_name.place(relx=0.5, rely=0.6, anchor='center')

            window_goal.after(10000, window_goal.destroy)
        else:
            messagebox.showinfo('Ошибка', 'Такого номера нет в списках игроков')

    def show_players(self):
        # Очищаем текстовое поле перед добавлением новых данных
        self.text_box_home.delete(1.0, tk.END)

        # Выводим игроков в текстовое поле
        count = 0
        for number, name in self.data_team.items():
            self.text_box_home.insert(tk.END, f"{count + 1}. {number} : {name}\n")
            count += 1

    def show_players2(self):
        # Очищаем текстовое поле перед добавлением новых данных
        self.text_box_guests.delete(1.0, tk.END)

        # Выводим игроков в текстовое поле
        count = 0
        for number, name in self.data_team2.items():
            self.text_box_guests.insert(tk.END, f"{count + 1}. {number} : {name}\n")
            count += 1

    def update_combo_box(self):
        self.goal_scored_number['values'] = list(self.data_team.keys())
        self.goal_scored_number2['values'] = list(self.data_team2.keys())
        self.penalty_number_entry['values'] = list(self.data_team.keys())
        self.penalty_number_entry2['values'] = list(self.data_team.keys())
        self.penalty_number_entry3['values'] = list(self.data_team.keys())
        self.penalty_number_entry4['values'] = list(self.data_team2.keys())
        self.penalty_number_entry5['values'] = list(self.data_team2.keys())
        self.penalty_number_entry6['values'] = list(self.data_team2.keys())

    def play_sound(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("sirena.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
