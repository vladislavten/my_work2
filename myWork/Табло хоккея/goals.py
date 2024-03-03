import os.path
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox



root = tk.Tk()
root.title("Гол забил")
root.geometry('400x200')

def save1():
    data[player_number_entry.get()] = player_name_entry.get()

def save2():
    data2[player_number_entry2.get()] = player_name_entry2.get()

def goal():
    if goal_scored_number.get() in data and os.path.exists(f'{os.path.dirname(__file__)}\\photo\\{goal_scored_number.get()}.jpg'):
        window_goal = tk.Toplevel(root)
        # window_goal.geometry('1280x1024')
        window_goal.attributes('-fullscreen', True)
        window_goal.title('ГОЛ')
        window_goal['bg'] = 'black'

        image_path = f"photo\\{goal_scored_number.get()}.jpg"
        image = Image.open(image_path)
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)

        photo_label = tk.Label(window_goal, image=photo)
        photo_label.image = photo  # сохраняем ссылку на изображение, чтобы избежать сборщика мусора
        photo_label.place(relx=0.5, rely=0.4, anchor='center')

        number1 = goal_scored_number.get()
        name1 = data[number1]

        goal_home = tk.Label(window_goal, text=f'Гол забил\nномер: {number1}, {name1} ', justify='center' ,font=("Helvetica", 50), bg="black", fg="red")
        goal_home.place(relx=0.5, rely=0.8, anchor='center')
        window_goal.after(3000, window_goal.destroy)
    elif goal_scored_number.get() in data:
        window_goal = tk.Toplevel(root)
        # window_goal.geometry('1280x1024')
        window_goal.attributes('-fullscreen', True)
        window_goal.title('ГОЛ')
        window_goal['bg'] = 'black'

        number1 = goal_scored_number.get()
        name1 = data[number1]

        goal_home = tk.Label(window_goal, text=f'Гол забил\nномер: {number1}, {name1} ', justify='center' ,font=("Helvetica", 50), bg="black", fg="red")
        goal_home.place(relx=0.5, rely=0.5, anchor='center')
        window_goal.after(3000, window_goal.destroy)
    else:
        # window_goal = tk.Toplevel(root)
        # window_goal.title("Фото")
        # window_goal.attributes('-fullscreen', True)
        # window_goal.configure(background='black')
        # no_name = tk.Label(window_goal, text=f'Гол забил номер: {goal_scored_number.get()} ', font=('Helvetica', 100), bg='black', fg='red')
        # no_name.place(relx=0.5, rely=0.5, anchor='center')
        # window_goal.after(3000, window_goal.destroy)
        print('Такого номера нет в списках игроков')
        messagebox.showinfo('Ошибка', 'Такого номера нет в списках игроков')


player_number_entry = tk.Entry(root)
player_number_entry.pack()
player_name_entry = tk.Entry(root)
player_name_entry.pack()
save_button = tk.Button(root, text="Записать 1", command=save1)
save_button.pack()

player_number_entry2 = tk.Entry(root)
player_number_entry2.pack()
player_name_entry2 = tk.Entry(root)
player_name_entry2.pack()
save_button2 = tk.Button(root, text="Записать 2", command=save2)
save_button2.pack()

goal_scored_number = tk.Entry(root)
goal_scored_number.pack()
goal_scored = tk.Button(root, text="Гол забил", command=goal)
goal_scored.pack()

data = {'23': 'Тен Владислав', '22': 'Тен Ульяна'}
data2 = {}

root.mainloop()


def list_save_comands(self):
    self.root2 = tk.Toplevel(root)
    self.root2.title("Гол забил")
    self.root2.geometry('400x400')

    def save1():
        self.data[self.player_number_entry.get()] = self.player_name_entry.get()
        print(self.data)

    def save2():
        self.data2[self.player_number_entry2.get()] = self.player_name_entry2.get()
        print(self.data2)

    def goal():
        if self.goal_scored_number.get() in self.data and os.path.exists(
                f'{os.path.dirname(__file__)}\\photo\\{self.goal_scored_number.get()}.jpg'):
            print('фото доступно')
            self.window_goal = tk.Toplevel(self.root2)
            self.window_goal.geometry('1280x1024')
            # window_goal.attributes('-fullscreen', True)
            self.window_goal.title('ГОЛ')
            self.window_goal['bg'] = 'black'

            self.image_path = f"photo\\{self.goal_scored_number.get()}.jpg"
            self.image = Image.open(self.image_path)
            self.image = self.image.resize((400, 400))
            self.photo = ImageTk.PhotoImage(self.image)

            self.photo_label = tk.Label(self.window_goal, image=self.photo)

            self.photo_label.image = self.photo  # сохраняем ссылку на изображение, чтобы избежать сборщика мусора

            self.photo_label.place(relx=0.5, rely=0.4, anchor='center')

            self.number1 = self.goal_scored_number.get()
            self.name1 = self.data[self.number1]
            print('ok6')

            self.goal_home = tk.Label(self.window_goal, text=f'Гол забил\nномер: {self.number1}, {self.name1} ',
                                      justify='center',
                                      font=("Helvetica", 50), bg="black", fg="red")
            self.goal_home.place(relx=0.5, rely=0.8, anchor='center')
            self.window_goal.after(3000, self.window_goal.destroy)
        elif self.goal_scored_number.get() in self.data:
            self.window_goal = tk.Toplevel(root)
            # window_goal.geometry('1280x1024')
            self.window_goal.attributes('-fullscreen', True)
            self.window_goal.title('ГОЛ')
            self.window_goal['bg'] = 'black'

            self.number1 = self.goal_scored_number.get()
            self.name1 = self.data[self.number1]

            self.goal_home = tk.Label(self.window_goal, text=f'Гол забил\nномер: {self.number1}, {self.name1} ',
                                      justify='center',
                                      font=("Helvetica", 50), bg="black", fg="red")
            self.goal_home.place(relx=0.5, rely=0.5, anchor='center')
            self.window_goal.after(3000, self.window_goal.destroy)
        else:
            print('Такого номера нет в списках игроков')
            messagebox.showinfo('Ошибка', 'Такого номера нет в списках игроков')

    self.player_number_entry = tk.Entry(self.root2)
    self.player_number_entry.pack()
    self.player_name_entry = tk.Entry(self.root2)
    self.player_name_entry.pack()
    self.save_button = tk.Button(self.root2, text="Записать 1", command=save1)
    self.save_button.pack()

    self.player_number_entry2 = tk.Entry(self.root2)
    self.player_number_entry2.pack()
    self.player_name_entry2 = tk.Entry(self.root2)
    self.player_name_entry2.pack()
    self.save_button2 = tk.Button(self.root2, text="Записать 2", command=save2)
    self.save_button2.pack()

    self.goal_scored_number = tk.Entry(self.root2)
    self.goal_scored_number.pack()
    self.goal_scored = tk.Button(self.root2, text="Гол забил", command=goal)
    self.goal_scored.pack()

    self.data = {'23': 'Тен Владислав', '22': 'Тен Ульяна'}
    self.data2 = {}
