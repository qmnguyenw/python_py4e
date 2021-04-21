Python | Remove substring list from String



Sometimes, while working with Python Strings, we can have problem in which we
need to remove a substring from String. This is quite easy and many times
solved before. But sometimes, we deal with list of strings that need to be
removed and String adjusted accordingly. Lets discuss certain ways in which
this task is achieved.

 **Method #1 : Using loop +replace()**  
The combination of above functions can be used to solve this problem. In this,
we perform the replace of multiple Strings as they occur using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove substring list from String

# Using loop + replace()

 

# initializing string

test_str = "gfg is best for all geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing sub list 

sub_list = ["best", "all"]

 

# Remove substring list from String

# Using loop + replace()

for sub in sub_list:

 test_str = test_str.replace(' ' + sub + ' ', ' ')

 

# printing result 

print("The string after substring removal : " + test_str)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best for all geeks
    The string after substring removal : gfg is for geeks
    

**Method #2 : Usingreplace() + join() + split()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of handling single space using join() + split().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove substring list from String

# Using replace() + join() + split()

 

# initializing string

test_str = "gfg is best for all geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing sub list 

sub_list = ["best", "all"]

 

# Remove substring list from String

# Using replace() + join() + split()

for sub in sub_list:

 test_str = test_str.replace(sub, ' ')

res = " ".join(test_str.split())

 

# printing result 

print("The string after substring removal : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best for all geeks
    The string after substring removal : gfg is for geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

