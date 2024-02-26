import tkinter as tk
from tkinter import messagebox
import time
import fouls


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

        self.button = tk.Button(master, text="Игра", command=self.general_start)
        self.button.pack()

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

        #######################################   КНОПКИ в окне master   ##########################################

        self.penalty_button = tk.Button(master, text="Записать штраф 1", command=self.penalty_apply)
        self.penalty_button.pack()

        self.penalty_button2 = tk.Button(master, text="Записать штраф 2", command=self.penalty_apply2)
        self.penalty_button2.pack()

        self.penalty_button3 = tk.Button(master, text="Записать штраф 3", command=self.penalty_apply3)
        self.penalty_button3.pack()

        self.penalty_button4 = tk.Button(master, text="Записать штраф 4", command=self.penalty_apply4)
        self.penalty_button4.pack()

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

        ############################### ПЕРЕМЕННЫЕЕЕЕЕЕЕЕЕЕЕЕЕЕ
        self.penalty_minutes = '0'
        self.penalty_minutes2 = '0'
        self.penalty_minutes3 = '0'
        self.penalty_minutes4 = '0'

        # self.penalty_number = ''
        #############################

    ##########################################  ФУНКЦИИ ##################################################

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
                    self.time_zero() #сброс тайминга штрафа
                    self.penalty_minutes = self.penalty_minutes_entry.get()
                    self.penalty_timer_label = tk.Label(self.timer_window, text=f"0{self.penalty_minutes}:00", font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label.place(relx=0.9, rely=0.8, anchor="center")
                    self.penalty_number = self.penalty_number_entry.get()
                    self.penalty_number_label = tk.Label(self.timer_window, text=self.penalty_number, font=("DS-Digital", 40), bg="black", fg="red")
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
                    self.time_zero2() #сброс тайминга штрафа
                    self.penalty_minutes2 = self.penalty_minutes_entry2.get()
                    self.penalty_timer_label2 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes2}:00", font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label2.place(relx=0.9, rely=0.7, anchor="center")
                    self.penalty_number2 = self.penalty_number_entry2.get()
                    self.penalty_number_label2 = tk.Label(self.timer_window, text=self.penalty_number2, font=("DS-Digital", 40), bg="black", fg="red")
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
                    self.time_zero3() #сброс тайминга штрафа
                    self.penalty_minutes3 = self.penalty_minutes_entry3.get()
                    self.penalty_timer_label3 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes3}:00", font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label3.place(relx=0.9, rely=0.6, anchor="center")
                    self.penalty_number3 = self.penalty_number_entry3.get()
                    self.penalty_number_label3 = tk.Label(self.timer_window, text=self.penalty_number3, font=("DS-Digital", 40), bg="black", fg="red")
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
                    self.time_zero4() #сброс тайминга штрафа
                    self.penalty_minutes4 = self.penalty_minutes_entry4.get()
                    self.penalty_timer_label4 = tk.Label(self.timer_window, text=f"0{self.penalty_minutes4}:00", font=("DS-Digital", 40), bg="black", fg="red")
                    self.penalty_timer_label4.place(relx=0.9, rely=0.5, anchor="center")
                    self.penalty_number4 = self.penalty_number_entry4.get()
                    self.penalty_number_label4 = tk.Label(self.timer_window, text=self.penalty_number4, font=("DS-Digital", 40), bg="black", fg="red")
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
                self.penalty_minutes = '0'  #Обязательно возращать 0 во все переменные штрафа
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
                self.penalty_minutes2 = '0'  #Обязательно возращать 0 во все переменные штрафа
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
                self.penalty_minutes3 = '0'  #Обязательно возращать 0 во все переменные штрафа
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
                self.penalty_minutes4 = '0'  #Обязательно возращать 0 во все переменные штрафа
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


