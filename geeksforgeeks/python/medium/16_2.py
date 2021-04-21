Python | How to time the program



This article aims to show how to calculate the time it takes to perform
various tasks.  
A simple solution to it is to use **time** module. This module contains
various time-related functions. Also it’s very useful to put a higher-level
interface over these functions and use them as a stop-watch as explained in
the code below –

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Using time module

import time

 

# defining the class

class Timer:

 

def __init__(self, func = time.perf_counter):

 self.elapsed = 0.0

 self._func = func

 self._start = None

 

# starting the module

def start(self):

 if self._start is not None:

 raise RuntimeError('Already started')

 self._start = self._func()

 

# stopping the timmer

def stop(self):

 if self._start is None:

 raise RuntimeError('Not started')

 end = self._func()

 self.elapsed += end - self._start

 self._start = None

 

# reseting the timmer

def reset(self):

 self.elapsed = 0.0

 @property

 

def running(self):

 return self._start is not None

 

def __enter__(self):

 self.start()

 return self

 

def __exit__(self, *args):

 self.stop()  
  
---  
  
 __

 __

We can start, stopped or reset this timer using this class as needed by the
user so as to keep a track of the total elapsed time in the elapsed attribute.
To do so, it is mentioned in the code below –

 **Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# using the class Timer()

def countdown(n):

 while n > 0:

 n -= 1

 

# Use 1: Explicit start / stop

time = Timer()

 

# start

time.start()

countdown(1000000)

 

# stop

time.stop()

print(time.elapsed)

 

# Use 2: As a context manager

with time:

 countdown(1000000)

 

print(time.elapsed)

 

with Timer() as t2:

 countdown(1000000)

 

print(t2.elapsed)  
  
---  
  
 __

 __

  * The code above gives a very simple but still very useful class for measuring the time and tracking elapsed time.  
It also illustrated how to support **contextmanagement** protocol and the
**with** statement.

  * The underlying time function is a concern while performing the time functions. As the accuracy of timing measurements made with functions such as **time.time()** or **time.clock()** varies according to the operating system.
  * The highest-resolution timer available on the system in contrast is used by **time.perf_counter()**.

To amount the CPU time used by process, **time.process_time()** is used
instead as explained in the code below:

  

  

 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

t= Timer(time.process_time)

with t:

 countdown(1000000)

print(t.elapsed)  
  
---  
  
 __

 __

Both the **time.perf_counter()** and **time.process_time()** return a “time”
in fractional seconds. To make sense of the results, call the functions twice
and compute a time difference as the actual value of the time doesn’t have any
particular meaning.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

