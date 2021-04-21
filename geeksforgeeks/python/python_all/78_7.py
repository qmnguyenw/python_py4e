Python – Distance between occurrences



Sometimes, while working with Python Strings, we can have a task in which we
need to find the indices difference between occurrences of a particular
character. This can have application in domains such as day-day programming.
Lets discuss certain ways in which this task can be done.

 **Method #1 : Usingindex()**  
This is one of the way in which we can solve this problem. In this, we use the
power of index() to get the Nth index of occurrence and subtract with initial
occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distance between occurrences

# Using index()

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'k'

 

# Distance between occurrences

# Using index()

res = test_str.index(K, test_str.index(K) + 1) -
test_str.index(K)

 

# printing result 

print("The character occurrence difference is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The character occurrence difference is : 8
    

**Method #2 : Usingfind() + rfind()**  
The combination of above functions can be used to solve this problem. In this,
we find the first occurrence using find() and next(last) using rfind().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distance between occurrences

# Using find() + rfind()

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'k'

 

# Distance between occurrences

# Using find() + rfind()

res = test_str.rfind(K) - test_str.find(K)

 

# printing result 

print("The character occurrence difference is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The character occurrence difference is : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

