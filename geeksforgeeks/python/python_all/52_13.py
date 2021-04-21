Python – Extract String till Numeric



Given a string, extract all its content till first appearance of numeric
character.

>  **Input** : test_str = “geeksforgeeks7 is best”  
>  **Output** : geeksforgeeks  
>  **Explanation** : All characters before 7 are extracted.
>
>  **Input** : test_str = “2geeksforgeeks7 is best”  
>  **Output** : “”  
>  **Explanation** : No character extracted as 1st letter is numeric.

 **Method #1 : Using isdigit() + index() + loop**

The combination of above functions can be used to solve this problem. In this,
we check for first occurrence of numeric using isdigit() and index() is used
to get required index till which content needs to be extracted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String till Numeric

# Using isdigit() + index() + loop

 

# initializing string

test_str = "geeks4geeks is best"

 

# printing original string

print("The original string is : " + str(test_str))

 

# loop to iterating characters

temp = 0

for chr in test_str:

 

 # checking if character is numeric,

 # saving index

 if chr.isdigit():

 temp = test_str.index(chr)

 

# printing result 

print("Extracted String : " + str(test_str[0 : temp]))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks is best
    Extracted String : geeks
    

**Method #2 : Using regex()**

This is yet another way in which this task can be performed. Using appropriate
regex(), one can get content before possible numerics.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String till Numeric

# Using regex()

import re

 

# initializing string

test_str = "geeks4geeks is best"

 

# printing original string

print("The original string is : " + str(test_str))

 

# regex to get all elements before numerics

res = re.findall('([a-zA-Z ]*)\d*.*', test_str)

 

# printing result 

print("Extracted String : " + str(res[0]))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks is best
    Extracted String : geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

