Python | Range duplication in String



Sometimes, while working with Strings, we can have a problem in which we need
to replicate the range of strings consecutively in range. This kind of problem
can have application in day-day programming domain. Lets discuss certain way
in which this task can be performed.

 **Method : Using string slicing**  
This is straight forward way to solve this problem. In this, we perform the
task of slicing the string to be repeated and attach its duplicate. The pre
and post slices are attached to its prefix and suffic respectively to
construct result string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Range duplication in String

# Using string slicing

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing range 

i, j = 3, 6

 

# Range duplication in String

# Using string slicing

temp = test_str[i:j] * 2

res = test_str[:i] + temp + test_str[j:]

 

# printing result 

print("The string after range duplication : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The string after range duplication : geeksfksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

