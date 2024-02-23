import tkinter as tk
from tkinter import messagebox
import time


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Управление Таймером")
        self.master.geometry("600x600")

        self.timer_window = tk.Toplevel(master)
        self.timer_window.title("Таймер")
        self.timer_window.geometry("1024x768")
        self.timer_window['bg'] = 'black'
        # self.timer_window.withdraw()

        self.timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 100), bg="black", fg="red")
        self.timer_label.pack(expand=True)
        self.timer_label.place(relx=0.5, rely=0.355, anchor="center")


        self.timer_running = False
        self.time_remaining = 20 * 60
        self.start_time = 0
        self.paused_time = 0

        self.penalty_timer_label = tk.Label(self.timer_window, text="00:00", font=("DS-Digital", 40), bg="black", fg="red")
        self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
        self.penalty_timer_label.place_forget()

        self.penalty_timer_running = False
        self.penalty_time_remaining = 0 # БЫЛО 20 * 60
        self.penalty_start_time = 0
        self.penalty_paused_time = 0

        #######################################   КНОПКИ в окне master   ##########################################

        self.penalty_button = tk.Button(master, text="Записать штраф", command=self.penalty_apply)
        self.penalty_button.pack()

        self.button = tk.Button(master, text="Игра", command=self.general_start)
        self.button.pack()

        ###########################################################

        self.penalty_minutes_entry = tk.Entry(master)
        self.penalty_minutes_entry.pack()

        self.penalty_update_timer()
        self.update_timer()

        ################################################################

        ############################### ПЕРЕМЕННЫЕ
        self.penalty_minutes = '0'
        #############################

    ##########################################  ФУНКЦИИ ##################################################

    def general_start(self):
        self.penalty_toggle_timer()
        self.toggle_timer()

    # def penalty_apply(self):
    #     if self.penalty_minutes_entry.get() == '2' or self.penalty_minutes_entry.get() == '4' or self.penalty_minutes_entry.get() == '5':
    #         self.penalty_minutes = self.penalty_minutes_entry.get()
    #         self.penalty_timer_label = tk.Label(self.timer_window, text=f"0{self.penalty_minutes}:00", font=("DS-Digital", 40), bg="black", fg="red")
    #         self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
    #     else:
    #         messagebox.showinfo("Информация", "Введены некоррктные данные")

    def penalty_apply(self):
        if not self.timer_running:
            self.penalty_minutes = self.penalty_minutes_entry.get()
            self.penalty_timer_label = tk.Label(self.timer_window, text=f"0{self.penalty_minutes}:00", font=("DS-Digital", 40), bg="black", fg="red")
            self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
        else:
            messagebox.showinfo('Ошибка', 'Нельзя вводить штрафное время пока идёт отсчет основного времени')



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


    def penalty_update_timer(self):
        if self.penalty_timer_running:
            elapsed_time = int(time.time() - self.penalty_start_time)
            self.penalty_time_remaining = max(0, int(self.penalty_minutes) * 6 - elapsed_time)
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))
            if self.penalty_time_remaining > 0:
                self.timer_window.after(1000, self.penalty_update_timer)
            else:
                self.penalty_timer_running = False
                self.penalty_minutes = '0'
                self.penalty_timer_label.place_forget()
                # self.penalty_button.config(text="Старт")
        else:
            self.penalty_timer_label.config(text=self.penalty_format_time(self.penalty_time_remaining))

    def penalty_format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(minutes, seconds)


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


