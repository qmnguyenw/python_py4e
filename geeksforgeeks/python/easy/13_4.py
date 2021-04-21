Python | Communicating Between Threads | Set-2



 **Prerequisite:** Communicating Between Threads | Set-1

If a thread needs to know immediately when a consumer thread has processed a
particular item of data, one should pair the sent data with an Event object
that allows the producer to monitor its progress as shown in the code given
below –

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

from queue import Queue

from threading import Thread, Event

 

# A thread that produces data

def producer(out_q):

 while running:

 # Produce some data

 ...

 # Make an (data, event) pair and 

 # hand it to the consumer

 evt = Event()

 out_q.put((data, evt))

 ...

 # Wait for the consumer to process the item

 evt.wait()

 

 # A thread that consumes data

 def consumer(in_q):

 while True:

 # Get some data

 data, evt = in_q.get()

 # Process the data

 ...

 # Indicate completion

 evt.set()  
  
---  
  
 __

 __

Writing threaded programs based on simple queuing is often a good way to
maintain sanity. If everything is broken down to simple thread-safe queuing,
it doesn’t need to litter the program with locks and other low-level
synchronization. Also, communicating with queues often leads to designs that
can be scaled up to other kinds of message-based communication patterns later
on. For instance, one can split the program into multiple processes, or even a
distributed system, without changing much of its underlying queuing
architecture.  
One caution with thread queues is that putting an item in a queue doesn’t make
a copy of the item. Thus, communication actually involves passing an object
reference between threads.

If the shared state is a concern, it may make sense to only pass immutable
data structures (e.g., integers, strings, or tuples) or to make deep copies of
the queued items as shown in the code given below :

  

  

 **Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

from queue import Queue

from threading import Thread

import copy

 

# A thread that produces data

def producer(out_q):

 while True:

 # Produce some data

 ...

 out_q.put(copy.deepcopy(data))

 

# A thread that consumes data

def consumer(in_q):

 while True:

 # Get some data

 data = in_q.get()

 # Process the data

 ...  
  
---  
  
 __

 __

  * Queue objects provide a few additional features that may prove to be useful in certain contexts.
  * If creating a Queue with an optional size, such as Queue(N), it places a limit on the number of items that can be enqueued before the put() blocks the producer.
  * Adding an upper bound to a queue might make sense if there is mismatch in speed between a producer and consumer.
  * For instance, if a producer is generating items at a much faster rate than they can be consumed.
  * On the other hand, making a queue block when it’s full can also have an unintended cascading effect throughout the program, possibly causing it to deadlock or run poorly.
  * In general, the problem of “flow control” between communicating threads is a much harder problem than it seems.
  * If ever trying to fix a problem by fiddling with queue sizes, it could be an indicator of a fragile design or some other inherent scaling problem.

 **Code #3 :get() and put() methods supporting nonblocking and timeouts.**

 __

 __  
 __

 __

 __  
 __  
 __

import queue

q = queue.Queue()

 

try:

 data = q.get(block = False)

except queue.Empty:

 ...

try:

 q.put(item, block = False)

except queue.Full:

 ...

 

try:

 data = q.get(timeout = 5.0)

except queue.Empty:

 ...  
  
---  
  
 __

 __

Both of these options can be used to avoid the problem of just blocking
indefinitely on a particular queuing operation. For example, a
nonblockingput() could be used with a fixed-sized queue to implement
different kinds of handling code for when a queue is full.

 **Code # 4: Issuing a log message and discarding**

 __

 __  
 __

 __

 __  
 __  
 __

def producer(q):

 ...

 try:

 q.put(item, block = False)

 except queue.Full:

 log.warning('queued item % r discarded !', item)  
  
---  
  
 __

 __

A timeout is useful if one is trying to make consumer threads periodically
give up on operations such as q.get() so that they can check things such as
a termination flag.

 **Code #5 : Using timeout**

 __

 __  
 __

 __

 __  
 __  
 __

_running= True

 

def consumer(q):

 while _running:

 try:

 item = q.get(timeout = 5.0)

 # Process item

 ...

 except queue.Empty:

 pass  
  
---  
  
 __

 __

Lastly, there are utility methodsq.qsize(), q.full(), q.empty() that can
tell the current size and status of the queue. However, be aware that all of
these are unreliable in a multithreaded environment. For example, a call to
q.empty() might tell that the queue is empty, but in the time that has
elapsed since making the call, another thread could have added an item to the
queue. Frankly, it’s best to write the code not to rely on such functions.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

