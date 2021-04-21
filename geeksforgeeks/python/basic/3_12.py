Python – Queue.LIFOQueue vs Collections.Deque



Both _LIFOQueue_ and _Deque_ can be used using in-built modules _Queue_ and
_Collections_ in Python, both of them are data structures and are widely used,
but for different purposes. In this article, we will consider the difference
between both _Queue.LIFOQueue_ and _Collections.Deque_ concerning usability,
execution time, working, implementation, etc. in Python.

 **queue.LifoQueue:** The module _queue_ provides a LIFO Queue which
technically works as a Stack. It is usually used for communication between the
different threads in the very same process.

 **Below is a program which depicts the implementation of** _ **Lifo.Queue**_
**:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required module

import queue

# Initialize LIFO Queue

LIFOq = queue.LifoQueue(maxsize=3)

# qsize() give the maxsize of

# the Queue

print(LIFOq.qsize())

# Data Inserted as 5->9->1->7,

# same as Queue

LIFOq.put(1)

LIFOq.put(2)

LIFOq.put(3)

# Displaying if the Queue is full

print("Full: ", LIFOq.full())

# Displaying size of queue

print("Size: ", LIFOq.qsize())

# Data will be accessed in the

# reverse order Reverse of that

# of Queue

print(LIFOq.get())

print(LIFOq.get())

print(LIFOq.get())

# Displaying if the queue is empty or not

print("Empty: ", LIFOq.empty())  
  
---  
  
 __

 __

 **Output:**

    
    
    0
    Full:  True
    Size:  3
    3
    2
    1
    Empty:  True

 **collections.deque:** Deque (Doubly Ended Queue) in Python is implemented
using the module _collections_. This data structure is mainly used for queues.
The FIFO queue mechanism is implemented by _append()_ and _popleft()_. It’s
operations are quite faster as compared to lists.

  

  

 **Below is a program that illustrates the implementation of** _
**collections.deque**_ **:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

import collections

# Initialize deque

Deque = collections.deque([10, 20, 30])

# Using append() to insert element at right end

# Inserts 0 at the end of deque

Deque.append(0)

# Printing modified deque

print("The deque after appending at right is:", Deque)

# Using appendleft() to insert element at left end

# Inserts 100 at the beginning of deque

Deque.appendleft(100)

# Printing modified deque

print("The deque after appending at left is: ", Deque)

# Using pop() to delete element from right end

# Deletes 0 from the right end of deque

Deque.pop()

# Printing modified deque

print("The deque after deleting from right is:", Deque);

# Using popleft() to delete element from left end

# Deletes 100 from the left end of deque

Deque.popleft()

# Printing modified deque

print("Queue:", Deque)  
  
---  
  
 __

 __

 **Output:**

    
    
    The deque after appending at right is: deque([10, 20, 30, 0])
    The deque after appending at left is:  deque([100, 10, 20, 30, 0])
    The deque after deleting from right is: deque([100, 10, 20, 30])
    Queue: deque([10, 20, 30])

###  **Difference between LIFOQueue and Deque:**

Sr. no.| LIFO Queue| Dequeue| 1| It implements stacks| It implements a double-
edged queue| 2| Present in _Queue_ module| Present in _Collections_ module| 3|
Allows various threads to communicate using queued data or messages| Simply
intended to be a data structure| 4| Fewer features (operations and methods)|
Large Variety of features (operations and methods)| 5| Follows Last In First
Out| Follows Fist In First Out| 6| Slow operations (long execution time)| High
operations(very low execution time)| 6| Not commonly used, usually used for
thread communication operations.| Mostly used for data structure operations.  
---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

