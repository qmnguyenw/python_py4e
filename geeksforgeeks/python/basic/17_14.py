Find size of a list in Python



In Python, List is a collection data-type which is ordered and changeable. A
list can have duplicate entry as well. Here, the task is find the number of
entries in a list. See the examples below.

Examples:

    
    
    Input : a = [1, 2, 3, 1, 2, 3]
    Output : 6
    Count the number of entries in the list a.
    
    Input : a = []
    Output : 0
    

The idea is to use len() in Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working

# of len()

a = []

a.append("Hello")

a.append("Geeks")

a.append("For")

a.append("Geeks")

print("The length of list is: ", len(a))  
  
---  
  
 __

 __

 **Output:**

    
    
    The length of list is:  4
    

Example 2:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate working

# of len()

n = len([10, 20, 30])

print("The length of list is: ", n)  
  
---  
  
 __

 __

 **Output:**

    
    
    The length of list is:  3
    

**How does len() work?**  
len() works in O(1) time as list is an object and has a member to store its
size. Below is description of len() from Python docs.

> Return the length (the number of items) of an object. The argument may be a
> sequence (such as a string, bytes, tuple, list, or range) or a collection
> (such as a dictionary, set, or frozen set).

 **How to check if a list is empty in Python**

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

