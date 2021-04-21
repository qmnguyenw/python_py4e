How to control PC from anywhere using Python?



 **Prerequisite –** **Socket programming in Python**

In this solution, we use the concept of Socket Programming for establishing
communication between two computers.

### **Socket Programming in Python**

Socket Programming is a way of connecting two systems on a network to
communicate with each other. Sockets are the endpoints built for sending and
receiving data and it is a combination of IP address and port. We will import
the socket module to use Socket Programming in Python. The following are the
methods required to build the solution:

 **Methods in Socket Module:** **Method**|  **Description**|
socket.socket().| Create sockets.| socket.bind()| This method bind hostname
and portname to socket.| socket.listen()| This method starts the TCP
listener.| socket.accept()| Accept client connection and wait until the
connection arrives.| socket.connect()| Initiate TCP connection.|
socket.close()| Close the socket.  
---|---  
  
 **Other Socket Methods:**

  

  
 **Method**|  **Description**|  s.recv()| It receives TCP message | s.send()|
It sends TCP message| socket.gethostname()| It returns hostname  
---|---  
  
So we have to develop two python programs one is **master.py** (server)and
another is **slave.py** (client), using master.py we can control the system
having slave.py program. To control the pc from anywhere using python please
the follow the step mentioned below:

 **Step 1: Create and Execute the “master.py” in one terminal**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

import socket

import sys

import os

 

# Initialize s to socket

s = socket.socket()

 

# Initialize the host

host = socket.gethostname()

 

# Initialize the port

port = 8080

 

# Bind the socket with port and host

s.bind(('', port))

 

print("waiting for connections...")

 

# listening for conections

s.listen()

 

# accepting the incoming connections

conn, addr = s.accept()

 

print(addr, "is connected to server")

 

# take command as input

command = input(str("Enter Command :"))

 

conn.send(command.encode())

 

print("Command has been sent successfully.")

 

# recieve the confrmation

data = conn.recv(1024)

 

if data:

 print("command recieved and executed sucessfully.")  
  
---  
  
 __

 __

 **Step 2:** **Create and Execute the “slave.py” is another terminal**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

import socket

import sys

import os

 

# Initialize s to socket

s = socket.socket()

 

# Initialize the host

host = "127.0.0.1"

 

# Initiaze the port

port = 8080

 

# bind the socket with port and host

s.connect((host, port))

 

print("Connected to Server.")

 

# recieve the command from master program

command = s.recv(1024)

command = command.decode()

 

# match the command and execute it on slave system

if command == "open":

 print("Command is :", command)

 s.send("Command recieved".encode())

 

 # you can give batch file as input here

 os.system('ls')  
  
---  
  
 __

 __

 **Output:**

![server terminal](https://media.geeksforgeeks.org/wp-
content/uploads/20200915214857/master.JPG)

terminal running master.py

![client terminal](https://media.geeksforgeeks.org/wp-
content/uploads/20200915214859/slave.JPG)

terminal running slave.py

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

