Python | Reverse Incremental String Slicing



Sometimes, while working with Pythonn strings, we can have a problem in which
we need to perform the slice and print of strings in reverse order. This can
have application in day-day programming. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate the list in reverse order and store the incremental strings in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Incremental String Slicing

# Using loop

 

# initializing string

test_str = "geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Reverse Incremental String Slicing

# Using loop

res = []

sub = ''

for chr in reversed(test_str):

 sub += chr

 res.append(sub)

 

# printing result 

print("The incremental reverse strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeks
    The incremental reverse strings : ['s', 'sk', 'ske', 'skee', 'skeeg']
    

**Method #2 : Using list slicing + list comprehension**  
This is yet another way in which this task can be performed. In this, we
iterate the string list using list comprehension and slicing is used to
perform incremental slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Incremental String Slicing

# Using list comprehension + list slicing

 

# initializing string

test_str = "geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Reverse Incremental String Slicing

# Using list comprehension + list slicing

res = [test_str[-1 : idx : -1] for idx in
range(-2, -2 - len(test_str), -1)]

 

# printing result 

print("The incremental reverse strings : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeks
    The incremental reverse strings : ['s', 'sk', 'ske', 'skee', 'skeeg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

