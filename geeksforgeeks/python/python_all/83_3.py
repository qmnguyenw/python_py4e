Python | Reverse Interval Slicing String



Sometimes, while working with strings, we can have a problem in which we need
to perform string slicing. In this we can have a variant in which we need to
perform reverse slicing that too interval. This kind of application can come
in day-day programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using String Slicing (1)**  
This task can be performed using string slicing, that too nested one. In this,
first slice to peform the Interval and second slice to perform reverse.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Interval Slicing String

# Using String Slicing 1

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing Interval

K = 2

 

# Reverse Interval Slicing String

# Using String Slicing 1

res = test_str[::K][::-1]

 

# printing result 

print("The reverse Interval Slice : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The reverse Interval Slice : segoseg
    

**Method #2 : Using String Slicing (2)**  
It is another way in which this task can be performed. In this, we employ
similar way as above, but a different kind of slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Interval Slicing String

# Using String Slicing 2

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing Interval

K = 2

 

# Reverse Interval Slicing String

# Using String Slicing 1

res = test_str[::-1][::K]

 

# printing result 

print("The reverse Interval Slice : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The reverse Interval Slice : segoseg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

