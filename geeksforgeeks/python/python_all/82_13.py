Python | Extract odd length words in String



Sometimes, while working with Python, we can have a problem in which we need
to extract certain length words from a string. This can be extraction of odd
length words from the string. This can have application in many domains
including day-day programming. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we first
split the string to words and then perform iteration to get the odd length
words.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract odd length words in String

# Using loop

 

# initializing string

test_str = "gfg is best of geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Extract odd length words in String

# Using loop

res = []

for ele in test_str.split():

 if len(ele) % 2 :

 res.append(ele)

 

# printing result 

print("The odd length strings are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best of geeks
    The odd length strings are : ['gfg', 'geeks']
    

**Method #2 : Using list comprehension**  
This task can also be performed using list comprehension. In this, we perform
the task in similar way as above. Just the difference is that its a one-liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract odd length words in String

# Using list comprehension

 

# initializing string

test_str = "gfg is best of geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Extract odd length words in String

# Using list comprehension

res = [ele for ele in test_str.split() if len(ele) %
2]

 

# printing result 

print("The odd length strings are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg is best of geeks
    The odd length strings are : ['gfg', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

