Find the size of a Dictionary in Python



Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only single
value as an element, Dictionary holds key:value pair. Key value is provided in
the dictionary to make it more optimized. The size of a Dictionary means the
amount of memory (in bytes) occupied by a Dictionary object. In this article,
we will learn various ways to get the size of a python Dictionary.

 **1.Usinggetsizeof() function:**

The getsizeof() function belongs to the python’s sys module. It has been
implemented in the below example.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

import sys

 

# sample Dictionaries

dic1 = {"A": 1, "B": 2, "C": 3} 

dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3":
"Deepanshu"}

dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4:
"Wolf"}

 

# print the sizes of sample Dictionaries

print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")

print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")

print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Size of dic1: 216bytes
    Size of dic2: 216bytes
    Size of dic3: 216bytes

 **1.Using inbuilt__sizeof__() method:**

Python also has an inbuilt __sizeof__() method to determine the space
allocation of an object without any additional garbage value. It has been
implemented in the below example.  
 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# sample Dictionaries

dic1 = {"A": 1, "B": 2, "C": 3} 

dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3":
"Deepanshu"}

dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4:
"Wolf"}

 

# print the sizes of sample Dictionaries

print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")

print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")

print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of dic1: 216bytes
    Size of dic2: 216bytes
    Size of dic3: 216bytes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

