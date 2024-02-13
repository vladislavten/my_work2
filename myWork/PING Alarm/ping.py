import tkinter as tk
from ping3 import ping
import threading
import winsound
import time

def ping_ip():
    ip_address = ip_entry.get()
    while ping_running:
        try:
            response = ping(ip_address)
            if response != False:
                print(f"Ping to {ip_address} successful. RTT: {response} ms")
                canvas.itemconfig(circle, fill="green")
            else:
                print("Ping failed.")
                canvas.itemconfig(circle, fill="red")
                winsound.PlaySound("alarm2.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print("Error:", str(e))
        time.sleep(0.3)

def start_ping():
    global ping_running
    ping_running = True
    ping_thread = threading.Thread(target=ping_ip)
    ping_thread.start()

def stop_ping():
    global ping_running
    ping_running = False
    canvas.itemconfig(circle, fill="gray")

def on_enter_pressed(event):
    start_ping()

root = tk.Tk()
root.title("Ping Tool")
root.geometry("300x300")

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(anchor='center')

circle = canvas.create_oval(75, 25, 125, 75, fill="gray")

ip_label = tk.Label(root, text="IP Address:")
ip_label.pack(anchor='center', pady=(20, 0))

ip_entry = tk.Entry(root)
ip_entry.pack(anchor='center')

error_label = tk.Label(root, text="", fg="red")
error_label.pack(anchor='center', pady=(10, 0))

ping_button = tk.Button(root, text="Start Ping", command=start_ping)
ping_button.pack(anchor='center', pady=(20, 0))

stop_button = tk.Button(root, text="Stop Ping", command=stop_ping)
stop_button.pack(anchor='center', pady=(10, 0))

ip_entry.bind("<Return>", on_enter_pressed)

root.mainloop()
