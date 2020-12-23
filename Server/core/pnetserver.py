#!/usr/bin/python

import socket
from pathlib import Path
import keyboard
from getpass import getpass

pwd = Path("key.txt")
if pwd.is_file():
    s = socket.socket()
    hostip = socket.gethostbyname(socket.gethostname())
    host = socket.gethostname()	      
    port = 9090			        

    s.bind((host,port))		   
    
    print("PNet server IP: " + hostip)
    print("Waiting for connection...")	
    s.listen(5)			 

    while True:
        conn,addr = s.accept()	     
        print('Got Connection from', addr)
        message = "Successfully connected to " + hostip
        conn.send(message.encode())
        conn.close()
            
else:
    password_provided = getpass("Enter a secure password: ")
    file = open(r"key.txt", "w")
    file.write(password_provided)
    file.close()

    s = socket.socket()		   
    hostip = socket.gethostbyname(socket.gethostname())
    host = socket.gethostname()	      
    port = 9090			        

    s.bind((host,port))		
    
    print("PNet server IP: " + hostip)
    print("Waiting for connection...")
    s.listen(5)			 

    while True:
        conn,addr = s.accept()	     
        print('Got Connection from', addr)
        message = "Successfully connected to " + hostip
        conn.send(message.encode())
        conn.close()