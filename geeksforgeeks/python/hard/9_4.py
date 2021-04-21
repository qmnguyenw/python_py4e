Barrier Objects in Python



Barrier objects in python are used to wait for a fixed number of thread to
complete execution before any particular thread can proceed forward with the
execution of the program. Each thread calls wait() function upon reaching the
barrier. The barrier is responsible for keeping track of the number of wait()
calls. If this number goes beyond the number of threads for which the barrier
was initialized with, then the barrier gives a way to the waiting threads to
proceed on with the execution. All the threads at this point of execution, are
simultaneously released.

Barriers can even be used to synchronize access between threads. However,
generally a barrier is used to combine the output of threads. A barrier object
can be reused multiple times for the exact same number of threads that it was
initially initialized for.

 **Initializing a barrier**

A barrier can be initialized using threading.Barrier class as shown in the
program below. The number within the parenthesis represents the number of the
threads that the barrier should wait upon.

 **Syntax:**

  

  

    
    
     **barrier = threading.Barrier(number_of_threads, action = None, timeout = None)**

Create a barrier object for the number_of_threads. An action, when provided,
is a callable to be called by one of the threads when they are released.
timeout is the default timeout value if none is specified for the wait()
method.

 __

 __  
 __

 __

 __  
 __  
 __

import threading

 

barrier = threading.Barrier(3)

 

class thread(threading.Thread):

 def __init__(self, thread_ID):

 threading.Thread.__init__(self)

 self.thread_ID = thread_ID

 def run(self):

 print(str(self.thread_ID) + "\n")

 barrier.wait()

 

thread1 = thread(100)

thread2 = thread(101)

 

thread1.start()

thread2.start()

barrier.wait()

 

print("Exit\n")  
  
---  
  
 __

 __

 **Output:**

    
    
     **100
    101
    Exit**

