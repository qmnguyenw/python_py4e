Making a Port-Scanner in Kali Linux Terminal Using Python



In computer networking, a **port** is a virtual point where network
connections start and end. It’s like an open door of your home, If you don’t
close this then anyone can Enter your home. A port scanner is a program that
is searching ports in a network and tries to find which ports are virtually
open and close. It is common technique hackers or cyber-security experts used
to discover open doors or weak points in a network.

### **How Does a Port Scanner Program Work?**

This program sends a network request throw network and tries to connect to a
specific TCP or UDP port on a computer and records the response.

The **three** types of responses are below:

  1.  **Open, Accepted** : When ports are open, and you can access this system by them.
  2.  **Closed, Not Listening** : When this port is in **use or unavailable** at this time
  3.  **Filtered, Dropped, Blocked** : The computer doesn’t even bother to respond.

###  **Design a Port Scanner on Kali Linux Terminal Using Python**

 **Step 1: Design a Program**

At the very first we need to open Our Kali Linux terminal and the very first
thing that we should do is find out where our python interpreter is so we
command

  

  

 **Syntax:**

    
    
    which python

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20201229160903/1-300x139.png)

where is our python interpreter

That’s going to be important when we do this very next step.

Next step we need to open the shell because in there we are going to type our
code, so we can type **nano** command and hit enter.

 **Syntax:**

    
    
    nano (name).extention

 **Example:**

    
    
    nano port-scanner.py

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20201229162030/2-300x139.png)

give our program a name

Now In here at first we need to assign our Python interpreter Location

    
    
    #!//usr/bin/python

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20201229163428/3-300x139.png)

location of Python interpreter

Now our main program start, we want to import sockets, sockets will tell us
the ports how to operate and essentially how to transmit data.

    
    
    import socket

Then we need to input IP addresses  and after that, we also need a program to
ask for which port we are looking for

  

  

    
    
    ip = raw_input("enter the IP Adress: ")
    port = input("Enter the Port Number: ")

Now we want to Define the socket what type of transmitted data are we are
looking for to be more specific what Protocol are we asking for to see.

  *  **socket.AF_INET** this socket allows us to see TCP connection
  *  **SOCK_STREAM** this allows us to look at UDP protocol that’s essentially streaming video and audio

    
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Now we are going to print how our program shows us if the specific port open
or either IP is down or The port is closed.

    
    
    if sock.connect_ex((ip,port)):
           print "Port ",port, "is closed"
    else:
             print"Port",port,"is OPEN"

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20201229180752/11-660x550.png)

full program

Now save this program press **control key + x key** to save this program

 **Syntax:**

    
    
    cnrl+x

 **Step 2: Compile and Run The program**

We all Know How to Run a Script on the Kali Linux terminal

**Example**

    
    
    ./script name . extention

 **Syntax**

    
    
    ./port-scanner.py

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-content/uploads/20210103203049/12.png)

Program Didn’t Run

Look here is the **tricky part** , We write Our program Perfectly, but it’s
Not compiled and Run. So It’s time to give our System Permission.

> **Chmod 775** is a Linux command which sets permission so that
> **User/Owner** can Read, Write and execute. **Group** can Read Write and
> execute. Others **** can Read But can’t Write and execute.

**Syntax**

    
    
    chmod 775 ./port-scanner.py

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20210104115437/13-300x250.png)

chmod 775 gives you permission

Now we can Run Our program again, and it will compile and Run Successfully

**Syntax**

    
    
    ./port-scanner.py

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20210104120258/141-300x250.png)

Run successfully

## Test Our program

So for port scanning, We need a **specific IP, and** we need to Tell Our
Program which **port** we are Looking For after Input Hit Enter

**Example**

    
    
    Enter Your Ip Adress : 192.168.43.1
    Enter The Port Number : 80

![ Design a port scanner on Kali Linux terminal by python
](https://media.geeksforgeeks.org/wp-
content/uploads/20210104120923/15-660x550.png)

Port scanning Successfully

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

