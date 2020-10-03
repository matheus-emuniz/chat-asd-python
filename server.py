import socket
from threading import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8080

server.bind((IP, PORT))

server.listen(20)

client_list = []

def client_thread(connection, addr):
    while True:
        message = connection.recv(2048)

        if message:
            print(f"<{addr[0]}> {message}")
            message_to_client = f"<{addr[0]}> {message}"
            broadcast(message_to_client, connection)

def broadcast():
    pass

while True:
    connection, addr = server.accept()

    t = Thread(target=client_thread, args=(connection, addr))

    client_list.append(connection)

    print(addr[0] + " connected")