Cristian’s Algorithm



 **Cristian’s Algorithm** is a clock synchronization algorithm is used to
synchronize time with a time server by client processes. This algorithm works
well with low-latency networks where Round Trip Time is short as compared to
accuracy while redundancy prone distributed systems/applications do not go
hand in hand with this algorithm. Here Round Trip Time refers to the time
duration between start of a Request and end of corresponding Response.

Below is an illustration imitating working of cristian’s algorithm:  
![Cristian's agorithm illustration](https://media.geeksforgeeks.org/wp-
content/uploads/Cristians_algorithm_illustration.png)

 **Algorithm:**

1) The process on the client machine sends the request for fetching clock
time(time at server) to the Clock Server at time
![T_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-43897facf7260323794a709c11d3ac74_l3.png).

2) The Clock Server listens to the request made by the client process and
returns the response in form of clock server time.

  

  

3) The client process fetches the response from the Clock Server at time
![T_1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f4298cc122b134829eb82d5e7bea5d06_l3.png) and calculates
the synchronised client clock time using the formula given below.

![ \\\[ T_{CLIENT} = T_{SERVER} + \(T_1 - T_0\)/2 \\\]
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-18b40d7e02831dd6a81f8643483c787f_l3.png)

where ![T_{CLIENT}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4fa5684a072f5e6522e32b2ceb34f8a0_l3.png) refers to the
synchronised clock time,  
![T_{SERVER}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-783956caefff8581efb8d819895b5469_l3.png) refers to the
clock time returned by the server,  
![T_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-43897facf7260323794a709c11d3ac74_l3.png) refers to the
time at which request was sent by the client process,  
![T_1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f4298cc122b134829eb82d5e7bea5d06_l3.png) refers to the
time at which response was received by the client process

 **Working/Reliability of above formula:**

![T_1 - T_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-258aa35ee0b04b8140eb90d48d337a78_l3.png) refers to the
combined time taken by the network and the server to transfer request to the
server, process the request and returning the response back to the client
process, assuming that the network latency
![T_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-43897facf7260323794a709c11d3ac74_l3.png) and
![T_1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f4298cc122b134829eb82d5e7bea5d06_l3.png) are
approximately equal.

The time at client side differs from actual time by at most ![\(T_1 -
T_0\)/2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c37b20ae2112cac96dec3f5e18df85a7_l3.png) seconds. Using
above statement we can draw a conclusion that the error in synchronisation can
be at most ![\(T_1 - T_0\)/2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c37b20ae2112cac96dec3f5e18df85a7_l3.png) seconds.  
Hence,

![ \\\[ error\\, \\epsilon\\, \[-\(T_1 - T_0\)/2, \\, \(T_1 - T_0\)/2\] \\\]
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-476cf18f368563acdaf63b14dae0981d_l3.png)

Python Codes below illustrate the working of Cristian’s algorithm:  
Code below is used to initiate a prototype of a clock server on local machine:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program imitating a clock server

 

import socket

import datetime

 

# function used to initiate the Clock Server

def initiateClockServer():

 

 s = socket.socket()

 print("Socket successfully created")

 

 # Server port

 port = 8000

 

 s.bind(('', port))

 

 # Start listening to requests

 s.listen(5) 

 print("Socket is listening...")

 

 # Clock Server Running forever

 while True: 

 

 # Establish connection with client

 connection, address = s.accept() 

 print('Server connected to', address)

 

 # Respond the client with server clock time

 connection.send(str(

 datetime.datetime.now()).encode())

 

 # Close the connection with the client process 

 connection.close()

 

 

# Driver function

if __name__ == '__main__':

 

 # Trigger the Clock Server 

 initiateClockServer()  
  
---  
  
 __

 __

 **Output:**

    
    
    Socket successfully created
    Socket is listening...
    

Code below is used to initiate a prototype of a client process on local
machine:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program imitating a client process

 

import socket 

import datetime

from dateutil import parser

from timeit import default_timer as timer

 

# function used to Synchronize client process time

def synchronizeTime():

 

 s = socket.socket() 

 

 # Server port

 port = 8000

 

 # connect to the clock server on local computer 

 s.connect(('127.0.0.1', port)) 

 

 request_time = timer()

 

 # receive data from the server

 server_time = parser.parse(s.recv(1024).decode())

 response_time = timer() 

 actual_time = datetime.datetime.now()

 

 print("Time returned by server: " + str(server_time))

 

 process_delay_latency = response_time - request_time

 

 print("Process Delay latency: " \

 + str(process_delay_latency) \

 + " seconds")

 

 print("Actual clock time at client side: " \

 + str(actual_time))

 

 # synchronize process client clock time

 client_time = server_time \

 + datetime.timedelta(seconds = \

 (process_delay_latency) / 2)

 

 print("Synchronized process client time: " \

 + str(client_time))

 

 # calculate synchronization error 

 error = actual_time - client_time

 print("Synchronization error : "

 + str(error.total_seconds()) + " seconds")

 

 s.close() 

 

 

# Driver function

if __name__ == '__main__':

 

 # synchronize time using clock server

 synchronizeTime()  
  
---  
  
 __

 __

 **Output:**

    
    
    Time returned by server: 2018-11-07 17:56:43.302379
    Process Delay latency: 0.0005150819997652434 seconds
    Actual clock time at client side: 2018-11-07 17:56:43.302756
    Synchronized process client time: 2018-11-07 17:56:43.302637
    Synchronization error : 0.000119 seconds
    

**Improvision in Clock Synchronization:**

Using iterative testing over the network, we can define a minimum transfer
time using which we can formulate an improved synchronization clock time(less
synchronization error).  
Here, by defining a minimum transfer time, with a high confidence, we can say
that the server time will  
always be generated after ![T_0 + T_{min}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-4182ee1d048170884708d16378d35383_l3.png) and
the ![T_{SERVER}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-783956caefff8581efb8d819895b5469_l3.png) will always be
generated before ![T_1 - T_{min}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8fae5f706e1e3deb0385181ad9db030d_l3.png), where
![T_{min}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f71ae6406e6b8c9694f626a9f250d0a9_l3.png) is the minimum
transfer time which is the minimum value of
![T_{REQUEST}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-9df029c814fc553eb65b59bad055fae2_l3.png) and
![T_{RESPONSE}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8f89ad54dff152860618fb7c77eab505_l3.png) during several
iterative tests. Here synchronization error can be formulated as follows:

![\\\[ error\\, \\epsilon\\, \[-\(\(T_1 - T_0\)/2 - T_{min}\), \\, \(\(T_1 -
T_0\)/2 - T_{min}\)\] \\\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-df72c8775f172461209e3fc0e769de27_l3.png)

Similarily, if ![T_{REQUEST}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-9df029c814fc553eb65b59bad055fae2_l3.png) and
![T_{RESPONSE}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8f89ad54dff152860618fb7c77eab505_l3.png) differ by a
considerable amount of time, we may substitute
![T_{min}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f71ae6406e6b8c9694f626a9f250d0a9_l3.png) by
![T_{min1}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-26143b291247f41f6463186eb3c2c390_l3.png) and
![T_{min2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-236589ac3575f413d4aa10451a2f598f_l3.png), where
![T_{min1}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-26143b291247f41f6463186eb3c2c390_l3.png) is the minimum
observed request time and ![T_{min2}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-236589ac3575f413d4aa10451a2f598f_l3.png)
refers to the minimum observed response time over the network.  
The synchronized clock time in this case can be calculated as:

![ \\\[ T_{CLIENT} = T_{SERVER} + \(T_1 - T_0\)/2 + \(T_{min2} - T_{min1}\)/2
\\\] ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-949cdd9ee2b55ab66bf57b8f5c2fb9be_l3.png)

So, by just introducing response and request time as separate time latencies,
we can improve synchronization of clock time and hence decrease the overall
synchronization error. Number of iterative tests to be ran depends on the
overall clock drift observed.

 **References:**  
1) https://en.wikipedia.org/wiki/Cristian%27s_algorithm  
2) https://en.wikipedia.org/wiki/Round-trip_delay_time  
3) https://www.geeksforgeeks.org/socket-programming-python  
4) https://en.wikipedia.org/wiki/Clock_drift

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

