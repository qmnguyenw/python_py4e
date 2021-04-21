LRU Cache in Python using OrderedDict



LRU (Least Recently Used) Cache discards the least recently used items first.
This algorithm requires keeping track of what was used when, which is
expensive if one wants to make sure the algorithm always discards the least
recently used item. General implementations of this technique require keeping
“age bits” for cache-lines and track the “Least Recently Used” cache-line
based on age-bits.  
Our problem statement is to design and implement a data structure for Least
Recently Used (LRU) cache.  
It should support the following operations: get and put.  
* **get(key)** – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.   
* **put(key, value)** – Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.  
The cache is always initialized with positive capacity.

 **Examples:**  

    
    
    **Input/Output :** 
    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);                                    
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    
    
    
    

Our solution is to use the power of OrderedDict from collections module which
keep order of insertion of keys and we can change that order if required. The
best part is all operations have O(1) time complexity.  
We maintain our OrderedDict in such a way that the order shows how recently
they were used. In the beginning, we will have least recently used and in the
end, most recently used.  
If any update OR query is made to a key it moves to the end (most recently
used). If anything is added, it is added at the end (most recently used/added)  
For get(key): we return the value of the key that is queried in O(1) and
return -1 if we don’t find the key in out dict/cache. And also move the key to
the end to show that it was recently used.  
For put(key, value): first, we add/ update the key by conventional methods.
And also move the key to the end to show that it was recently used. But here
we will also check whether the length of our ordered dictionary has exceeded
our capacity, If so we remove the first key (least recently used)  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict

class LRUCache:

 # initialising capacity

 def __init__(self, capacity: int):

 self.cache = OrderedDict()

 self.capacity = capacity

 # we return the value of the key

 # that is queried in O(1) and return -1 if we

 # don't find the key in out dict / cache.

 # And also move the key to the end

 # to show that it was recently used.

 def get(self, key: int) -> int:

 if key not in self.cache:

 return -1

 else:

 self.cache.move_to_end(key)

 return self.cache[key]

 # first, we add / update the key by conventional methods.

 # And also move the key to the end to show that it was recently used.

 # But here we will also check whether the length of our

 # ordered dictionary has exceeded our capacity,

 # If so we remove the first key (least recently used)

 def put(self, key: int, value: int) -> None:

 self.cache[key] = value

 self.cache.move_to_end(key)

 if len(self.cache) > self.capacity:

 self.cache.popitem(last = False)

# RUNNER

# initializing our cache with the capacity of 2

cache = LRUCache(2)

cache.put(1, 1)

print(cache.cache)

cache.put(2, 2)

print(cache.cache)

cache.get(1)

print(cache.cache)

cache.put(3, 3)

print(cache.cache)

cache.get(2)

print(cache.cache)

cache.put(4, 4)

print(cache.cache)

cache.get(1)

print(cache.cache)

cache.get(3)

print(cache.cache)

cache.get(4)

print(cache.cache)

#This code was contributed by Sachin Negi  
  
---  
  
 __

 __

 **Output:**

    
    
    OrderedDict([(1, 1)])
    OrderedDict([(1, 1), (2, 2)])
    OrderedDict([(2, 2), (1, 1)])
    OrderedDict([(1, 1), (3, 3)])
    OrderedDict([(1, 1), (3, 3)])
    OrderedDict([(3, 3), (4, 4)])
    OrderedDict([(3, 3), (4, 4)])
    OrderedDict([(4, 4), (3, 3)])
    OrderedDict([(3, 3), (4, 4)])
    
    

Time Complexity :O(1)  
Other implementation of LRU  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

