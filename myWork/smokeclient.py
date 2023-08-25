import socket
import tkinter as tk

def handle_response(response):
    if response == b"1":
        tk.messagebox.showinfo("Результат", "Да")
    else:
        tk.messagebox.showinfo("Результат", "Нет")

def send_request():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    data = client_socket.recv(1024)
    handle_response(data)

root = tk.Tk()
button = tk.Button(root, text="Пойдем курить?", command=send_request)
button.pack()
root.mainloop()
