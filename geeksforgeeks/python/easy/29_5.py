Program to calculate the Round Trip Time (RTT)



 **Round trip time(RTT)** is the length of time it takes for a signal to be
sent plus the length of time it takes for an acknowledgement of that signal to
be received. This time therefore consists of the propagation times between the
two point of signal.  
On the Internet, an end user can determine the RTT to and from an IP(Internet
Protocol) address by pinging that address. The result depends on various
factors :-

  * The data rate transfer of the source’s internet connection.
  * The nature of transmission medium.
  * The physical distance between source and destination.
  * The number of nodes between source and destination.
  * The amount of traffic on the LAN(Local Area Network) to which end user is connected.
  * The number of other requests being handled by intermediate nodes and the remote server.
  * The speed with which intermediate node and the remote server function.
  * The presence of Interference in the circuit.

Examples:

    
    
    Input : www.geeksforgeeks.org
    Output : Time in seconds : 0.212174892426
    
    Input : www.cricbuzz.com
    Output : Time in seconds : 0.55425786972
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to calculate RTT

 

import time

import requests

 

# Function to calculate the RTT

def RTT(url):

 

 # time when the signal is sent

 t1 = time.time()

 

 r = requests.get(url)

 

 # time when acknowledgement of signal 

 # is received

 t2 = time.time()

 

 # total time taken

 tim = str(t2-t1)

 

 print("Time in seconds :" + tim)

 

# driver program 

# url address

url = "http://www.google.com"

RTT(url)  
  
---  
  
 __

 __

Output:

    
    
      Time in seconds :0.0579478740692
    
    

  

  

This article is contributed by **Pramod Kumar**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

