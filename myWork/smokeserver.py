import socket
import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as tkMessageBox


def handle_client(client_socket, addr):
    response = tkMessageBox.askyesno("Пойдем курить?", "Вы хотите пойти курить?")
    if response == "yes":
        client_socket.sendall(b"1")
    else:
        client_socket.sendall(b"0")
    client_socket.close()

def start_server():
    HOST = '127.0.0.1'
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket, addr)

root = tk.Tk()
button = tk.Button(root, text="Пойдем курить?", command=start_server)
button.pack()
root.mainloop()
