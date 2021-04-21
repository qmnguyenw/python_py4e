Python – Slice from Last Occurrence of K



Sometimes, while working with Python Strings, we can have a problem in which
we need to perform the task of performing characters stripping on the last
occurrence of element. This can have applications in which data is involved.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + string slicing**  
The combination of above methods can be used to solve this problem. In this,
we search for the last occurrence using loop and save index to later slice.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice from Last Occurrence of K

# Using string slicing and loop

 

# initializing string

test_str = 'geeksforgeeks-is-best-for-geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "-"

 

# Slice from Last Occurrence of K

# Using string slicing and loop

idx = None

for i in range(len(test_str)):

 if K == test_str[i]:

 idx = i

res = test_str[:idx]

 

# printing result 

print("Sliced String is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks-is-best-for-geeks
    Sliced String is : geeksforgeeks-is-best-for
    

**Method #2 : Usingrfind() \+ string slicing**  
The combination of above methods can be used to solve this problem. In this,
we extract the last occurrence using rfind() and rest slicing as above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice from Last Occurrence of K

# Using rfind() + string slicing

 

# initializing string

test_str = 'geeksforgeeks-is-best-for-geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "-"

 

# Slice from Last Occurrence of K

# Using rfind() + string slicing

idx = test_str.rfind(K)

res = test_str[:idx]

 

# printing result 

print("Sliced String is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks-is-best-for-geeks
    Sliced String is : geeksforgeeks-is-best-for
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

