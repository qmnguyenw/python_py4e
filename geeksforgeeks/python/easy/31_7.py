ChainMap in Python



Python contains a container called “ **ChainMap** ” which encapsulates many
dictionaries into one unit. ChainMap is member of module “ **collections** “.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# ChainMap 

 

 

from collections import ChainMap 

 

 

d1 = {'a': 1, 'b': 2} 

d2 = {'c': 3, 'd': 4} 

d3 = {'e': 5, 'f': 6} 

 

# Defining the chainmap 

c = ChainMap(d1, d2, d3) 

 

print(c)  
  
---  
  
 __

 __

 **Output:**

    
    
    ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    

**Let’s see various Operations on ChainMap**

## Access Operations

 ****

  

  

* keys() :-

