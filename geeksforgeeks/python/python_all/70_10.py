Find the size of a list – Python



In Python, a list is a collection data type that can store elements in an
ordered manner and can also have duplicate elements. The size of a list means
the amount of memory (in bytes) occupied by a list object. In this article, we
will learn various ways to get the size of a python list.

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

 

# sample lists

list1 = [1, 2, 3, 5]

list2 = ["GeeksForGeeks", "Data Structure", "Algorithms"]

list3 = [1, "Geeks", 2, "For", 3, "Geeks"]

 

# print the sizes of sample lists

print("Size of list1: " + str(sys.getsizeof(list1)) +
"bytes")

print("Size of list2: " + str(sys.getsizeof(list2)) +
"bytes")

print("Size of list3: " + str(sys.getsizeof(list3)) +
"bytes")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Size of list1: 96bytes
    Size of list1: 88bytes
    Size of list1: 112bytes

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

# sample lists

list1 = [1, 2, 3, 5]

list2 = ["GeeksForGeeks", "Data Structure", "Algorithms"]

list3 = [1, "Geeks", 2, "For", 3, "Geeks"]

 

# print the sizes of the sample lists

print("Size of list1: " + str(list1.__sizeof__()) + "bytes")

print("Size of list2: " + str(list2.__sizeof__()) + "bytes")

print("Size of list3: " + str(list3.__sizeof__()) + "bytes")  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of list1: 72bytes
    Size of list1: 64bytes
    Size of list1: 88bytes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

