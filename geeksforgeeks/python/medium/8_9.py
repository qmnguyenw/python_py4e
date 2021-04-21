Clear LRU Cache in Python



The **LRU** is the Least Recently Used cache. LRU Cache is a type of high-
speed memory, that is used to quicken the retrieval speed of frequently used
data. It is implemented with the help of Queue and Hash data structures.

Note: For more information, refer to Python – LRU Cache

## How can one interact with the LRU Cache in Python?

Python’s **functool** module has provided functionality to interact with the
LRU Cache since Python 3.2. The functool module offers a decorator that can be
placed atop a Class of a function in Python. When used on functions that
require large amounts of variable access and change operations, using the LRU
Cache offers massive speed-up.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import functools

 

@functools.lru_cache(maxsize = None)

def gfg():

 # insert function logic here

 pass  
  
---  
  
 __

 __

Alternatively, the maxsize can be changed to suit one’s own preference. The
value is measured in kbs, and maxsize takes an integer argument

  

  

## Clearing LRU Cache

After the use of the cache, cache_clear() can be used for clearing or
invalidating the cache.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

import functools

 

@functools.lru_cache(maxsize = None)

def fib(n): 

 if n < 2: 

 return n 

 return fib(n-1) + fib(n-2)

 

fib(30)

 

# Before Clearing

print(fib.cache_info())

 

fib.cache_clear()

 

# After Clearing

print(fib.cache_info())  
  
---  
  
 __

 __

 **Output:**

    
    
    CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
    CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)

 **Example 2:** Additionally one can also call cache_clear() from another
function as well

 __

 __  
 __

 __

 __  
 __  
 __

import functools

 

@functools.lru_cache(maxsize = None)

def fib(n): 

 if n < 2: 

 return n 

 return fib(n-1) + fib(n-2)

 

def gfg():

 fib.cache_clear()

 

fib(30)

 

# Before Clearing

print(fib.cache_info())

 

gfg()

 

# After Clearing

print(fib.cache_info())  
  
---  
  
 __

 __

 **Output:**

    
    
    CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
    CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)

These methods have limitations as they are individualized, and the
cache_clear() function must be typed out for each and every LRU Cache
utilizing the function. We can overcome this problem, by using Python’s
inbuilt garbage collection module to collect all objects that have LRU Cache
Wrappers, and iteratively clear each object’s cache.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import gc

import functools

 

@functools.lru_cache(maxsize = None)

def gfg():

 # insert function logic here

 pass

 

@functools.lru_cache(maxsize = None)

def gfg1():

 # insert function logic here

 pass

 

@functools.lru_cache(maxsize = None)

def gfg2():

 # insert function logic here

 pass

 

gfg()

gfg1()

gfg2()

 

gc.collect()

 

# All objects collected

objects = [i for i in gc.get_objects() 

 if isinstance(i, functools._lru_cache_wrapper)]

 

# All objects cleared

for object in objects:

 object.cache_clear()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

