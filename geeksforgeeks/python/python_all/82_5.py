Python – Word starting at Index



Sometimes, while working with Python, we can have a problem in which we need
to extract the word which is starting from a particular index. This can have a
lot of application in school programming. Lets discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this we
iterate for the string after getting index till the first space.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word starting at Index

# Using loop

 

# initializing string

test_str = "gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 7

 

# Word starting at Index

# Using loop

res = ''

for idx in range(K, len(test_str)):

 if test_str[idx] == ' ':

 break

 res += test_str[idx]

 

# printing result 

print("Word at index K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best for geeks
    Word at index K : best
    

**Method #2 : Usingsplit() \+ list slicing**  
This is one of the way in which this task can be performed. In this, list
slicing is use to extract all characters after K and split is used to extract
the first word amongst them.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word starting at Index

# Using split() + list slicing

 

# initializing string

test_str = "gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 7

 

# Word starting at Index

# Using split() + list slicing

res = test_str[K:].split()[0]

 

# printing result 

print("Word at index K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best for geeks
    Word at index K : best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

