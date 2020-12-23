#usr/bin/python

import socket
from getpass import getpass
from cryptography.fernet import Fernet

s = socket.socket()		
#host = socket.gethostname()	        
port = 9090			      

def connect():
    host = input("Enter the PNet address: ")
    password_provided = getpass("Enter the PNet server password: ")
    file = open(r"../../Server/core/key.txt", "r")
    password = file.read()
    
    try:
        if password_provided == password:
            s.connect((host,port))
            print(s.recv(1024).decode())
       
        else:
            print("Invalid credentials!")
        
            s.close()

    except:
        print("Host address incorrect! Try again.")
        connect()
        
connect()