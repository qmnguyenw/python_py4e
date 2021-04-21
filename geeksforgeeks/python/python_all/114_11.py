Python | Get positional characters from String



Sometimes, while working with Python strings, we can have a problem in which
we need to create a substring by joining the particular index elements from a
string. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute method in which this task can be performed. In this, we run a
loop over the indices list and join the corresponding index characters from
string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get positional characters from String

# using loop

 

# initializing string 

test_str = "gfgisbest"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing index list 

indx_list = [1, 3, 4, 5, 7]

 

# Get positional characters from String

# using loop

res = ''

for ele in indx_list:

 res = res + test_str[ele]

 

# printing result

print("Substring of selective characters : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gfgisbest
    Substring of selective characters : fisbs
    

**Method #2 : Using generator expression +enumerate()**  
The combination of above functionalities can be used to perform this task. In
this, we run a loop using generator expression and indices extraction is done
with help of enumerate().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get positional characters from String

# using generator expression + enumerate()

 

# initializing string 

test_str = "gfgisbest"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing index list 

indx_list = [1, 3, 4, 5, 7]

 

# Get positional characters from String

# using generator expression + enumerate()

res = ''.join((char for idx, char in enumerate(test_str) if
idx in indx_list))

 

# printing result

print("Substring of selective characters : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gfgisbest
    Substring of selective characters : fisbs
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

