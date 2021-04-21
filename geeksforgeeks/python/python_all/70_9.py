Find the size of a Set in Python



A Set is an unordered collection data type that is iterable, mutable, and has
no duplicate elements. Python’s set class represents the mathematical notion
of a set. The size of a set means the amount of memory (in bytes) occupied by
a set object. In this article, we will learn various ways to get the size of a
python set.

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

 

# sample Sets

Set1 = {"A", 1, "B", 2, "C", 3}

Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3",
"Deepanshu"}

Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

 

# print the sizes of sample Sets

print("Size of Set1: " + str(sys.getsizeof(Set1)) + "bytes")

print("Size of Set2: " + str(sys.getsizeof(Set2)) + "bytes")

print("Size of Set3: " + str(sys.getsizeof(Set3)) + "bytes")  
  
---  
  
 __

 __

Output:

  

  

    
    
    Size of Set1: 736bytes
    Size of Set2: 736bytes
    Size of Set3: 224bytes

 **Note:** The sys.getsizeof() function includes the marginal space usage,
which includes the garbage collection overhead for the object. Meaning it
returns the total space occupied by the object in addition to the garbage
collection overhead for the spaces being used.

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

import sys

 

# sample Sets

Set1 = {"A", 1, "B", 2, "C", 3}

Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3",
"Deepanshu"}

Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

 

# print the sizes of sample Sets

print("Size of Set1: " + str(Set1.__sizeof__()) + "bytes")

print("Size of Set2: " + str(Set2.__sizeof__()) + "bytes")

print("Size of Set3: " + str(Set3.__sizeof__()) + "bytes")  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of Set1: 712bytes
    Size of Set2: 712bytes
    Size of Set3: 200bytes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

