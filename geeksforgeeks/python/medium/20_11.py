Python program to find the highest 3 values in a dictionary



Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only single
value as an element, Dictionary holds key:value pair.

 **Examples:**

    
    
    **Input :** my_dict = {'A': 67, 'B': 23, 'C': 45,
                       'D': 56, 'E': 12, 'F': 69} 
    
    **Output :** {'F': 69, 'A': 67, 'D': 56}
    

Let’s see differnet methods we can find the highest 3 values in a dictionary.  
  
**Method #1:** Using collections.Counter()

A **Counter** is a dict subclass for counting hashable objects. It is an
unordered collection where elements are stored as dictionary keys and their
counts are stored as dictionary values. Counts are allowed to be any integer
value including zero or negative counts. The Counter class is similar to bags
or multisets in other languages.

most_common([n]) returns a list of the _n_ most common elements and their
counts from the most common to the least.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# finding 3 highest values in a Dictionary 

 

from collections import Counter

 

# Initial Dictionary

my_dict = {'A': 67, 'B': 23, 'C': 45, 

 'D': 56, 'E': 12, 'F': 69}

 

k = Counter(my_dict)

 

# Finding 3 highest values

high = k.most_common(3) 

 

print("Initial Dictionary:")

print(my_dict, "\n")

 

 

print("Dictionary with 3 highest values:")

print("Keys: Values")

 

for i in high:

 print(i[0]," :",i[1]," ")  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial Dictionary:
    {'C': 45, 'B': 23, 'D': 56, 'A': 67, 'E': 12, 'F': 69} 
    
    Dictionary with 3 highest values:
    Keys: Values
    F  : 69  
    A  : 67  
    D  : 56
    

  
**Method #2:** Using heapq.nlargest()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# finding 3 highest values in a Dictionary 

from heapq import nlargest

 

# Initial Dictionary

my_dict = {'A': 67, 'B': 23, 'C': 45,

 'D': 56, 'E': 12, 'F': 69}

 

print("Initial Dictionary:")

print(my_dict, "\n")

 

ThreeHighest = nlargest(3, my_dict, key = my_dict.get)

 

print("Dictionary with 3 highest values:")

print("Keys: Values")

 

for val in ThreeHighest:

 print(val, ":", my_dict.get(val))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial Dictionary:
    {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67} 
    
    Dictionary with 3 highest values:
    Keys: Values
    F : 69
    A : 67
    D : 56
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

