import socket
import sys
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP = "127.0.0.1"
PORT = 8080


nickname = input("Digite seu nickname: ")

if len(nickname) > 0:
    server.connect((IP, PORT))

print("COMANDOS:\n MSG: -> Enviar mensagem \n PRIVATE:<nick> -> Enviar mensagem privada \n NICK:<novo-nick> -> Trocar de nickame \n SNDFILE:<nick>:<nome_arquivo> -> Envia arquivo \n RECFILE:<nick>:<ip>:<port>:<nome_arquivo> -> Recebe arquivo")

while True:
    for sock in [sys.stdin, server]:
        if sock == server:
            message = sock.recv(2048)
            print(message)
        else:
            message = input("> ")
            mensagem_desmembrada = message.split(":")
            tamanho_mensagem = len(mensagem_desmembrada)
            command = mensagem_desmembrada[0]
            if tamanho_mensagem == 3:   #SNDFILE
                destinatario = mensagem_desmembrada[1].lstrip()
                message = mensagem_desmembrada[2].lstrip()
            elif tamanho_mensagem > 3:  #RECFILE
                destinatario = mensagem_desmembrada[1].lstrip()
                ip = mensagem_desmembrada[2].lstrip()
                port = mensagem_desmembrada[3].lstrip()
                arquivo = mensagem_desmembrada[4].lstrip()
            else:
                message = mensagem_desmembrada[1].lstrip()
        if command == "MSG":
            server.send(pickle.dumps(message))
            print(f"{nickname}: {message}")
        elif command == "PRIVATE":
            pass
        elif command == "NICK":
            nickname = message
            print(f"Seu novo nickname é: {message}")
        elif command == "SNDFILE":
            pass
        elif command == "RECFILE":
            pass
        else:
            print("Comando inexistente")

            