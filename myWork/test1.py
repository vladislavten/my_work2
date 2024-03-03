import os.path
import tkinter as tk
from PIL import Image, ImageTk



root = tk.Tk()
root.title("Гол забил")
root.geometry('400x200')

def save1():
    data[number_entry.get()] = name_entry.get()

def save2():
    data2[number_entry2.get()] = name_entry2.get()

def goal():
    if goal_scored_number.get() in data:
        number1 = goal_scored_number.get()
        name1 = data[number1]
        window_goal = tk.Toplevel(root)
        window_goal.geometry('1280x1024')
        window_goal.title('ГОЛ')
        window_goal['bg'] = 'black'
        goal_home_label = tk.Label(window_goal, text=f'Гол забил\nномер: {number1}, {name1} ', justify='center' ,font=("Helvetica", 50), bg="black", fg="red")
        goal_home_label.place(relx=0.5, rely=0.5, anchor='center')
        window_goal.after(3000, window_goal.destroy)


number_entry = tk.Entry(root)
number_entry.pack()
name_entry = tk.Entry(root)
name_entry.pack()
save_button = tk.Button(root, text="Записать 1", command=save1)
save_button.pack()

number_entry2 = tk.Entry(root)
number_entry2.pack()
name_entry2 = tk.Entry(root)
name_entry2.pack()
save_button2 = tk.Button(root, text="Записать 2", command=save2)
save_button2.pack()

goal_scored_number = tk.Entry(root)
goal_scored_number.pack()
goal_scored = tk.Button(root, text="Гол забил", command=goal)
goal_scored.pack()

data = {'23': 'Тен Владислав', '22': 'Тен Ульяна'}
data2 = {}

root.mainloop()
