Python – Right and Left Shift characters in String



Sometimes, while working with Python Strings, we can have problem in which we
have both right and left rotate count of characters in String and would like
to know the resultant condition of String. This type of problem occurs in
competitive programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using String multiplication + string slicing**  
The combination of above functions can be used to perform this task. In this,
we multiple string thrice, perform the concatenation and selectively slice
string to get required result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Right and Left Shift characters in String

# Using String multiplication + string slicing

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing right rot 

r_rot = 7

 

# initializing left rot 

l_rot = 3

 

# Right and Left Shift characters in String

# Using String multiplication + string slicing

res = (test_str * 3)[len(test_str) + r_rot - l_rot : 

 2 * len(test_str) + r_rot - l_rot]

 

# printing result 

print("The string after rotation is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The string after rotation is : sforgeeksgeek
    

**Method #2 : Using % operator and string slicing**  
The combination of above functionalities can also be used to perform this
task. In this, we find the mod of rotation difference with length to compute
the string position.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Right and Left Shift characters in String

# Using % operator and string slicing

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing right rot 

r_rot = 7

 

# initializing left rot 

l_rot = 3

 

# Right and Left Shift characters in String

# Using % operator and string slicing

temp = (r_rot - l_rot) % len(test_str)

res = test_str[temp : ] + test_str[ : temp]

 

# printing result 

print("The string after rotation is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The string after rotation is : sforgeeksgeek
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

