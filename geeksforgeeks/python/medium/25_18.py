Socket Programming with Multi-threading in Python



 _Prerequisite :Socket Programming in Python_, Multi-threading in Python

 **Socket Programming** -> It helps us to connect a client to a server. Client
is message sender and receiver and server is just a listener that works on
data sent by client.

 **What is a Thread?**  
A thread is a light-weight process that does not require much memory overhead,
they are cheaper than processes.

 **What is Multi-threading Socket Programming?**  
Multithreading is a process of executing multiple threads simultaneously in a
single process.

 **Multi-threading Modules :**  
A __thread module & threading module_ is used for multi-threading in python,
these modules help in synchronization and provide a lock to a thread in use.

  

  

    
    
    from _thread import *
    import threading
    

A lock object is created by->

    
    
    print_lock = threading.Lock()
    

A lock has two states, “locked” or “unlocked”. It has two basic methods
acquire() and release(). When the state is unlocked **print_lock.acquire()**
is used to change state to locked and **print_lock.release()** is used to
change state to unlock.

The function **thread.start_new_thread()** is used to start a new thread and
return its identifier. The first argument is the function to call and its
second argument is a tuple containing the positional list of arguments.

Let’s study client-server multithreading socket programming by code-  
 _Note:-The code works with python3._

 **Multi-threaded Server Code**

 __

 __  
 __

 __

 __  
 __  
 __

# import socket programming library

import socket

 

# import thread module

from _thread import *

import threading

 

print_lock = threading.Lock()

 

# thread function

def threaded(c):

 while True:

 

 # data received from client

 data = c.recv(1024)

 if not data:

 print('Bye')

 

 # lock released on exit

 print_lock.release()

 break

 

 # reverse the given string from client

 data = data[::-1]

 

 # send back reversed string to client

 c.send(data)

 

 # connection closed

 c.close()

 

 

def Main():

 host = ""

 

 # reverse a port on your computer

 # in our case it is 12345 but it

 # can be anything

 port = 12345

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 s.bind((host, port))

 print("socket binded to port", port)

 

 # put the socket into listening mode

 s.listen(5)

 print("socket is listening")

 

 # a forever loop until client wants to exit

 while True:

 

 # establish connection with client

 c, addr = s.accept()

 

 # lock acquired by client

 print_lock.acquire()

 print('Connected to :', addr[0], ':', addr[1])

 

 # Start a new thread and return its identifier

 start_new_thread(threaded, (c,))

 s.close()

 

 

if __name__ == '__main__':

 Main()  
  
---  
  
 __

 __

    
    
    Console Window:
    socket binded to port 12345
    socket is listening
    Connected to : 127.0.0.1 : 11600
    Bye

 **Client Code**

 __

 __  
 __

 __

 __  
 __  
 __

# Import socket module

import socket

 

 

def Main():

 # local host IP '127.0.0.1'

 host = '127.0.0.1'

 

 # Define the port on which you want to connect

 port = 12345

 

 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

 

 # connect to server on local computer

 s.connect((host,port))

 

 # message you send to server

 message = "shaurya says geeksforgeeks"

 while True:

 

 # message sent to server

 s.send(message.encode('ascii'))

 

 # messaga received from server

 data = s.recv(1024)

 

 # print the received message

 # here it would be a reverse of sent message

 print('Received from the server
:',str(data.decode('ascii')))

 

 # ask the client whether he wants to continue

 ans = input('\nDo you want to continue(y/n) :')

 if ans == 'y':

 continue

 else:

 break

 # close the connection

 s.close()

 

if __name__ == '__main__':

 Main()  
  
---  
  
 __

 __

    
    
    Console Window:
    Received from the server : skeegrofskeeg syas ayruahs
    
    Do you want to continue(y/n) :y
    Received from the server : skeegrofskeeg syas ayruahs
    
    Do you want to continue(y/n) :n
    
    Process finished with exit code 0

Reference->  
https://docs.python.org/2/library/thread.html

This article is contributed by **SHAURYA UPPAL**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

