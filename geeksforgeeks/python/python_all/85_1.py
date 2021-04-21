Python – Remove all consonants from string



Sometimes, while working with Python, we can have a problem in which we wish
to remove all the non vowels from strings. This is quite popular question and
solution to it is useful in competitive programming and day-day programming.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this, we
iterate through the list and then check for non presence of vowels and filter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove all consonents from string

# Using loop

 

# initializing string

test_str = "Gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Remove all consonents from string

# Using loop

res = []

for chr in test_str:

 if chr in "aeiouAEIOU":

 res.extend(chr)

res = "".join(res)

 

# printing result 

print("String after consonents removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best for geeks
    String after consonents removal : ieoee
    

**Method #2 : Using list comprehension**  
This is one of the ways in which this task can be performed. In this, we
iterate through the list and then filter out vowels in similar manner but in
one-liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove all consonents from string

# Using list comprehension

 

# initializing string

test_str = "Gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Remove all consonents from string

# Using list comprehension

res = "".join([chr for chr in test_str if chr in "aeiouAEIOU"])

 

# printing result 

print("String after consonents removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best for geeks
    String after consonents removal : ieoee
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

