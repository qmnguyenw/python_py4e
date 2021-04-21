Python – Consecutive element deletion strings



Sometimes, while working with Python, we can have a problem in which we have a
string and wish to extract all possible combination of words after deletion of
consecutive elements one at a time. This can have application in many domains.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension + list slicing**  
This is one of the way in which this task can be performed. In this, we
iterate for the elements of list and keep on creating new string using
consecutive list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element deletion strings

# Using list comprehension + list slicing

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Consecutive element deletion strings

# Using list comprehension + list slicing

res = [test_str[: idx] + test_str[idx + 1:] 

 for idx in range(len(test_str))]

 

# printing result 

print("Consecutive Elements removal list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Geeks4Geeks  
> Consecutive Elements removal list : [‘eeks4Geeks’, ‘Geks4Geeks’,
> ‘Geks4Geeks’, ‘Gees4Geeks’, ‘Geek4Geeks’, ‘GeeksGeeks’, ‘Geeks4eeks’,
> ‘Geeks4Geks’, ‘Geeks4Geks’, ‘Geeks4Gees’, ‘Geeks4Geek’]

  

  

**Method #2 : Using list comprehension +enumerate()**  
The combination of above methods can be used to perform this task. In this, we
extract the index using enumerate. This gives more cleaner code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element deletion strings

# Using list comprehension + enumerate()

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Consecutive element deletion strings

# Using list comprehension + enumerate()

res = [test_str[:idx] + test_str[idx + 1:] 

 for idx, _ in enumerate(test_str)]

 

# printing result 

print("Consecutive Elements removal list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Geeks4Geeks  
> Consecutive Elements removal list : [‘eeks4Geeks’, ‘Geks4Geeks’,
> ‘Geks4Geeks’, ‘Gees4Geeks’, ‘Geek4Geeks’, ‘GeeksGeeks’, ‘Geeks4eeks’,
> ‘Geeks4Geks’, ‘Geeks4Geks’, ‘Geeks4Gees’, ‘Geeks4Geek’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

