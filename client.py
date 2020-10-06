import socket
import pickle
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "127.0.0.1"
PORT = 8080

server.connect((IP, PORT))

print("COMANDOS:\n MSG: -> Enviar mensagem \n PRIVATE:<nick> -> Enviar mensagem privada \n NICK:<novo-nick> -> Trocar de nickame \n SNDFILE:<nick>:<nome_arquivo> -> Envia arquivo \n RECFILE:<nick>:<ip>:<port>:<nome_arquivo> -> Recebe arquivo")

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for sock in read_sockets:
        if sock == server:
            message = sock.recv(2048)
            message = pickle.loads(message)
            
            print(message)
        else:
            message = input("> ")
            if message == "EXIT":
                server.close()
                exit()
            server.send(pickle.dumps(message))
            