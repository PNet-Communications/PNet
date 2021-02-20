import socket

HEADER = 64
PORT = 9090
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = input("[PNet] CLIENT: Server IP: ")
PASS = input("[PNet] SERVER: Enter password: ")
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg, pwd=False):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    #Error here
    if pwd == True:
        if client.recv(2048).decode(FORMAT) == "[PNet] CLIENT ERROR: Password incorrect.":
            connected = False
        if client.recv(2048).decode(FORMAT) == f"[PNet] CLIENT: Successfully connected to {SERVER}":
            connected = True

send(PASS, pwd=True)

while connected:
    msg = input("[PNet] CLIENT: Send a message: ")
    if msg != DISCONNECT_MESSAGE:
        send(msg, pwd)
    else:
        send(msg, pwd)
        connected = False