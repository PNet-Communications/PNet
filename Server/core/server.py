import socket
import threading
from requests import get
import uuid
HEADER = 64
PORT = 9090
#To connect over the internet change SERVER to your public IP
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, password):
    waiting = True
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            while waiting:
                print(f"[PNet] CONNECTING: {addr} attempting to connect...")
                if msg != password:
                    waiting = False
                    connected = False
                    conn.send("[PNet] CLIENT ERROR: Password incorrect.".encode(FORMAT))
                if msg == password:
                    waiting = False
                    connected = True
                    conn.send(f"[PNet] CLIENT: Successfully connected to {SERVER}".encode(FORMAT))
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send(f"[PNet] CLIENT: Successfully disconnected from {SERVER}".encode(FORMAT))
            print(f"[PNet] {addr}: {msg}")
            conn.send("[PNet] CLIENT: Message received.".encode(FORMAT))
    conn.close()
    
def start():
    print("[PNet] STARTING: Server is starting...")
    print("[PNet] STARTING: Generating key...")
    password = str(uuid.uuid4())
    print(f"[PNet] FINALIZING: Key generated: {password}")
    server.listen()
    print(f"[PNet] LISTENING: Server is listening on {SERVER}.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, password))
        thread.start()
        #print(f"[PNet] ACTIVE CONNECTIONS: {threading.activeCount() - 1}")
        
start()