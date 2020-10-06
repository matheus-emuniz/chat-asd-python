import socket
from threading import *
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8080

server.bind((IP, PORT))

server.listen(200)

client_list = []

def has_nick(connection):
    return find_client(connection)["nick"] != ""

def compare_nick(nick):
    for client in client_list:
        if client["nick"] == nick:
            return False
    return True

def find_client(connection):
    for client in client_list:
        if client["connection"] == connection:
            return client

def find_connection_by_nick(nick):
    for client in client_list:
        if client["nick"] == nick:
            return client["connection"]
    
def client_thread(connection, addr):
    connection.send(pickle.dumps("Bem-vindo ao chat!"))
    while True:
        try:
            message = connection.recv(2048)
            message = pickle.loads(message)
        except:
            pass
        
        if message:
            client = find_client(connection)
            try:
                mensagem_desmembrada = message.split(":")
                tamanho_mensagem = len(mensagem_desmembrada)
                command = mensagem_desmembrada[0]

                command = command.upper()

                if tamanho_mensagem == 3:   #SNDFILE / PRIVATE
                    destinatario = mensagem_desmembrada[1].lstrip()
                    conteudo = mensagem_desmembrada[2].lstrip()
                elif tamanho_mensagem > 3:  #RECFILE
                    destinatario = mensagem_desmembrada[1].lstrip()
                    ip = mensagem_desmembrada[2].lstrip()
                    port = mensagem_desmembrada[3].lstrip()
                    arquivo = mensagem_desmembrada[4].lstrip()
                elif tamanho_mensagem == 1: #EXIT
                    pass
                else:
                    conteudo = mensagem_desmembrada[1].lstrip()

                if has_nick(connection):
                    if command == "MSG":
                        nick = client["nick"]
                        message_to_client = pickle.dumps(f"<{nick}>: {conteudo}")
                        broadcast(message_to_client, connection)
                        print(f"{conteudo}")
                    elif command == "PRIVATE":
                        rec_connection = find_connection_by_nick(destinatario)
                        if rec_connection is None:
                            connection.send(pickle.dumps("Nickname não existe"))
                            continue
                        send_nick = client["nick"]
                        rec_connection.send(pickle.dumps(f"PRIVATE: <{send_nick}>: {conteudo}"))
                    elif command == "SNDFILE":
                        pass
                    elif command == "RECFILE":
                        pass
                    else:
                        print("Comando inexistente")
                if command == "NICK":
                    nickname = conteudo.rstrip()
                    if not compare_nick(nickname):
                        client["connection"].send(pickle.dumps("Nick já existente"))
                        continue
                    client["nick"] = nickname
                    connection.send(pickle.dumps(f"Seu novo nickname é: {nickname}"))
                    broadcast(pickle.dumps(f"<{nickname}> Entrou no servidor!!"), connection)
            except:
                client["connection"].send(pickle.dumps("Comando Inválido"))
            
        else:
            remove(connection)
            
def broadcast(message, connection): 
    for client in client_list: 
        if client["connection"]!=connection and client["nick"] != "": 
            try: 
                client["connection"].send(message) 
            except:
                client["connection"].close() 
        else:
            remove(client) 

def remove(client): 
    if connection in client_list: 
        client_list.remove(client) 

while True:
    connection, addr = server.accept()

    t = Thread(target=client_thread, args=(connection, addr))

    t.start()

    client_list.append({
        "connection": connection,
        "ip": addr,
        "nick": ""
    })

connection.close()
server.close()