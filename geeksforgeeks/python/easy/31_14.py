OrderedDict in Python



An **OrderedDict** is a dictionary subclass that remembers the order that keys
were first inserted. The only difference between dict() and OrderedDict() is
that:

OrderedDict **preserves the order** in which the keys are inserted. A regular
dict doesn’t track the insertion order, and iterating it gives the values in
an arbitrary order. By contrast, the order the items are inserted is
remembered by OrderedDict.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of OrderedDict

from collections import OrderedDict

 

print("This is a Dict:\n")

d = {}

d['a'] = 1

d['b'] = 2

d['c'] = 3

d['d'] = 4

 

for key, value in d.items():

 print(key, value)

 

print("\nThis is an Ordered Dict:\n")

od = OrderedDict()

od['a'] = 1

od['b'] = 2

od['c'] = 3

od['d'] = 4

 

for key, value in od.items():

 print(key, value)  
  
---  
  
 __

 __

Output:

    
    
    This is a Dict:
    ('a', 1)
    ('c', 3)
    ('b', 2)
    ('d', 4)
    
    This is an Ordered Dict:
    ('a', 1)
    ('b', 2)
    ('c', 3)
    ('d', 4)
    

**Important Points:**

  1.  **Key value Change:** If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of key

# value change in OrderedDict

from collections import OrderedDict

 

print("Before:\n")

od = OrderedDict()

od['a'] = 1

od['b'] = 2

od['c'] = 3

od['d'] = 4

for key, value in od.items():

 print(key, value)

 

print("\nAfter:\n")

od['c'] = 5

for key, value in od.items():

 print(key, value)  
  
---  
  
 __

 __

Output:

  

  

    
        Before:
    
    ('a', 1)
    ('b', 2)
    ('c', 3)
    ('d', 4)
    
    After:
    
    ('a', 1)
    ('b', 2)
    ('c', 5)
    ('d', 4)

  2.  **Deletion and Re-Inserting** : Deleting and re-inserting the same key will push it to the back as OrderedDict however maintains the order of insertion.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of deletion

# re-inserion in OrderedDict

from collections import OrderedDict

 

print("Before deleting:\n")

od = OrderedDict()

od['a'] = 1

od['b'] = 2

od['c'] = 3

od['d'] = 4

 

for key, value in od.items():

 print(key, value)

 

print("\nAfter deleting:\n")

od.pop('c')

for key, value in od.items():

 print(key, value)

 

print("\nAfter re-inserting:\n")

od['c'] = 3

for key, value in od.items():

 print(key, value)  
  
---  
  
 __

 __

Output:

    
        Before deleting:
    
    ('a', 1)
    ('b', 2)
    ('c', 3)
    ('d', 4)
    
    After deleting:
    
    ('a', 1)
    ('b', 2)
    ('d', 4)
    
    After re-inserting:
    
    ('a', 1)
    ('b', 2)
    ('d', 4)
    ('c', 3)
    
    

**Other Considerations** :

  * Ordered dict in Python version 2.7 consumes more memory than normal dict. This is due to the underlying Doubly Linked List implementation for keeping the order. In Python 2.7 Ordered Dict is not dict subclass, it’s a specialized container from collections module.
  * Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.
  * Ordered Dict can be used as a stack with the help of _popitem_ function. Try implementing LRU cache with Ordered Dict.

This article is contributed by **Sri Sanketh Uppalapati**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

