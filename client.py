import socket
import sys
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP = "127.0.0.1"
PORT = 8080


nickname = input("Digite seu nickname: ")
if len(nickname) > 0:
    server.connect((IP, PORT))

while True:
    for sock in [sys.stdin, server]:
        if sock == server:
            message = sock.recv(2048)
            print(message)
        else:
            message = input("> ")
            server.send(pickle.dumps(message))
            print(f"Você: {message}")