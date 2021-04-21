Python Program that Sends And Recieves Message from Client



Socket programming is a way of connecting two nodes on a network to
communicate with each other. One socket(node) listens on a particular port at
an IP, while the other socket reaches out to the other to form a connection.
The server forms the listener socket while the client reaches out to the
server.

Socket programming is started by importing the socket library and making a
simple socket.

    
    
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

Here we made a socket instance and passed it two parameters. The first
parameter is **AF_INET** and the second one is **SOCK_STREAM**. **AF_INET**
refers to the address family ipv4. The SOCK_STREAM means connection-oriented
TCP protocol.

 **Note:** For more information, refer to Socket Programming in Python

 **Now we can connect to a server using Server:**

  

  

A Server is a program that provides service to other computers on the network
or Internet. Similarly, a client is a program that receives services from the
server. When a server wants to communicate with a client, there is a need for
a socket. A socket is a point of connection between the server and the client.

 **  
TCP/IP server program that sends message to the client.  
**

 __

 __  
 __

 __

 __  
 __  
 __

import socket

 

# take the server name and port name

host = 'local host'

port = 5000

 

# create a socket at server side

# using TCP / IP protocol

s = socket.socket(socket.AF_INET, 

 socket.SOCK_STREAM)

 

# bind the socket with server

# and port number

s.bind(('', port))

 

# allow maximum 1 connection to

# the socket

s.listen(1)

 

# wait till a client accept

# connection

c, addr = s.accept()

 

# display client address

print("CONNECTION FROM:", str(addr))

 

# send message to the client after 

# encoding into binary string

c.send(b"HELLO, How are you ? \

 Welcome to Akash hacking World")

 

msg = "Bye.............."

c.send(msg.encode())

 

# disconnect the server

c.close()  
  
---  
  
 __

 __

 **  
TCP/IP server program that receive message from server.  
**

 __

 __  
 __

 __

 __  
 __  
 __

import socket

 

# take the server name and port name

 

host = 'local host'

port = 5000

 

# create a socket at client side

# using TCP / IP protocol

s = socket.socket(socket.AF_INET,

 socket.SOCK_STREAM)

 

# connect it to server and port 

# number on local computer.

s.connect(('127.0.0.1', port))

 

# receive message string from

# server, at a time 1024 B

msg = s.recv(1024)

 

# repeat as long as message

# string are not empty

while msg:

 print('Recived:' + msg.decode())

 msg = s.recv(1024)

 

# disconnect the client

s.close()  
  
---  
  
 __

 __

 **Note:** Open In Two Separate DOS Windows And First Execute server, then
Execute client.

 **Output of Server:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200201201728/server12.png)

 **Output of Client:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200201201743/client1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

