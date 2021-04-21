Python | Same and Different value space



In Python, we have same pool for similar values, even if they share different
variables. This has many advantages, that it saves a lot of memory arranging
different spaces for similar values. This is provided for small integers. But
there are ways in which we can have same and different pool values. Lets
discuss certain cases of the same.

 **Case #1 : Same pool ( Using + operator )**  
In this, when we create a String using “+” operator, we create a space that
will point to similar space in memory.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Same and Different value space

# Same value case

 

# initializing strings

test_str1 = "gfg"

 

# printing original string

print("The original string is : " + test_str1)

 

# Using + to construct second string 

test_str2 = "g" + "fg"

 

# testing values 

res = test_str1 is test_str2

 

# printing result 

print("Are values pointing to same pool ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg
    Are values pointing to same pool ? : True
    

**Case #2 : Different Pool ( Usingjoin() + ord() )**  
This is way in which we need to initialize string pointing to different value
space in memory. This can be achieved using join() for joining ASCII values
extracted using ord().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Same and Different value space

# Different value case

 

# initializing strings

test_str1 = "abc"

 

# printing original string

print("The original string is : " + test_str1)

 

# Using join() + ord() to construct second string 

test_str2 = ''.join((chr(idx) for idx in range(97,
100)))

 

# testing values 

res = test_str1 is test_str2

 

# printing result 

print("Are values pointing to same pool ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : abc
    Are values pointing to same pool ? : False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

