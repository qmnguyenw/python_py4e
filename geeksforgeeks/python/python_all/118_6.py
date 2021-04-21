Python | Print Alphabets till N



Sometimes, while working with Python, we can have a problem in which we need
to print specific number of alphabets in order. This can have application in
school level programming. Let’s discuss certain ways in which this problem can
be solved.

 **Method #1 : Using loop +chr()**  
This is brute force way to perform this task. In this, we iterate the elements
till which we need to print and concatenate the strings accordingly after
conversion to character using chr().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Print Alphabets till N

# Using loop

 

# initialize N 

N = 20

 

# printing N 

print("Number of elements required : " + str(N))

 

# Print Alphabets till N

# Using loop

res = ""

for idx in range(97, 97 + N):

 res = res + chr(idx) 

 

# printing result

print("Alphabets till N are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of elements required : 20
    Alphabets till N are : abcdefghijklmnopqrst
    

**Method #2 : Using string.ascii_lowercase + slicing**  
Combination of above functionalities can also be used to perform this task. In
this, we use inbuilt function to get extract the lowercase string and extract
the N characters using slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Print Alphabets till N

# Using string.ascii_lowercase + slicing

import string

 

# initialize N 

N = 20

 

# printing N 

print("Number of elements required : " + str(N))

 

# Print Alphabets till N

# Using string.ascii_lowercase + slicing

res = string.ascii_lowercase[:N]

 

# printing result

print("Alphabets till N are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of elements required : 20
    Alphabets till N are : abcdefghijklmnopqrst
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

